from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from pydantic import BaseModel, Field
from typing import List

from app.database.conections import Base

class SEvent(BaseModel):
    id: int = Field(default=None, primary_key=True)
    title: str 
    image: str 
    description: str
    tags: List[str]
    location: str 


    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "title": "FastAPI framework",
                    "image": "https://linktomyimage.com/image.png",
                    "description": "Text",
                    "tags": ["python", "fastapi"],
                    "location": "Orel, Russia"
                }
            ]
        }
    }





class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    image = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(JSONB)
    location = Column(String, nullable=False)