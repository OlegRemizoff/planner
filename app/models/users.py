from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from app.database.conections import Base





class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False) 
    hashed_password = Column(String, nullable=False)




class SUserAuth(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "fastapi@packt.com",
                    "password": "Stro0ng!",
                }
            ]
        }
    }







