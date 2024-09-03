import requests


# Проверка орфографии с помощью Яндекс Спеллер
YANDEX_SPELLER_API_URL = "https://speller.yandex.net/services/spellservice.json/checkText"


async def check_text(text: str):
    payload = {'text': text}
    response = requests.get(YANDEX_SPELLER_API_URL, params=payload)
    if response.status_code == 200:
        data = response.json()
        if data:
            corrected_text = text
            for error in data:
                if error['s']:
                    corrected_text = corrected_text.replace(
                        error['word'], error['s'][0])
            return corrected_text

    return text
