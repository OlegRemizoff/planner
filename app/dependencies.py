from fastapi import Request, HTTPException, Depends, status
import requests
from jose import jwt, JWTError
from datetime import datetime
from app.config import settings
from app.dao.planner_dao import UsersDAO


# Получение токена
def get_token(requests: Request):
    token = requests.cookies.get("events_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


# Получение текущего пользователя
async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get('exp')
    if not (expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


# Проверка орфографии с помощью Яндекс Спеллер
YANDEX_SPELLER_API_URL = "https://speller.yandex.net/services/spellservice.json/checkText"


async def check_text(text: str):
    payload = {'text': text}
    # print("\x1b[31;1m" + "До исправления   " + "\x1b[0m", text)
    response = requests.get(YANDEX_SPELLER_API_URL, params=payload)
    data = response.json()
    if data:
        corrected_text = text
        for error in data:
            if error['s']:
                corrected_text = corrected_text.replace(
                    error['word'], error['s'][0])
        # print("\x1b[31;1m" + "После исправления" + "\x1b[0m", corrected_text)
        return corrected_text

    return text



