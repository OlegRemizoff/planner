from fastapi import APIRouter, HTTPException, status
from app.models.users import User, UserSignIn


router = APIRouter(
    prefix="/users",
    tags=["User"]
)


users = {}

# Регистрация
@router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    users[data.email] = data
    return {
            "message": "User successfully registered!"
        }


# Авторизация
@router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return {
        "message": "User signed in successfully"
    }