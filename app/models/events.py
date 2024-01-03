from sqlmodel import JSON, SQLModel, Field, Column, Text
from typing import Optional, List


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    descripton: str =  Field(nullable=True)
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    model_config = {
        # arbitrary_types - это параметр в Python, используемый при сериализации объектов с помощью модуля pickle
        # позволяет сериализать произвольные типы объектов, включая пользоватские классы, функции и другие объекты
        "arbitrary_types_allowed": True,
        "orm_mode": True,
        "json_schema_extra": {
            "examples": [
                { 
                    "title": "FastAPI Book Launch",
                    "image": "https://linktomyimage.com/image.png",
                    "description": "Some text",
                    "tags": ["python", "fastapi"],
                    "location": "Google Meet"
                }
            ]
        }
    }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    # description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "FastAPI Book Launch",
                    "image": "https://linktomyimage.com/image.png",
                    "description": "BlaBlaBla...",
                    "tags": ["python", "fastapi"],
                    "location": "Google Meet"
                }
            ]
        }
    }

