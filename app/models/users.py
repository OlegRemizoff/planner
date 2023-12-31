from pydantic import BaseModel, EmailStr



class User(BaseModel):
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


class UserSignIn(BaseModel):
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



