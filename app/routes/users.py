from fastapi import APIRouter, HTTPException, Response, Depends, status
from app.models.users import SUserAuth, Users
from app.dao.planner_dao import UsersDAO
from app.auth import get_password_hash, create_access_token, authenticate_user
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


# Регистрация
@router.post("/register")
async def register_user(user_data: SUserAuth) -> dict:
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email exists"
        )
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    return {"message": "Operation has been successfully completed"}


# Авторизация
@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("events_access_token", access_token, httponly=True)
    return {"access_token": access_token}


# Выход из аккаунта
@router.post("/logout")
async def login_user(response: Response) -> dict:
    response.delete_cookie("events_access_token")
    return {"message": "Logout has been success!"}



# Получение информации о пользователе
@router.get("/get")
async def get_user(user: Users = Depends(get_current_user)):
    print(user, type(user), user.email)