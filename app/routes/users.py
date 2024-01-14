from fastapi import APIRouter, HTTPException, status
from app.models.users import SUserRegister
from app.dao.planner_dao import  UsersDAO
from app.auth import get_password_hash


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)




# Регистрация
@router.post("/register")
async def register_user(user_data: SUserRegister) -> dict:
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="User with supplied username exists"
                )
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    return {"message": "Operation has been successfully completed"}




