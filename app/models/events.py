from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from pydantic import BaseModel
from typing import List, Optional

from app.database.conections import Base

class SEvent(BaseModel):
    id: int
    title: str 
    image: str 
    description: str
    tags: List[str]
    location: str 


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 0,
                    "title": "FastAPI Book Launch",
                    "image": "https://linktomyimage.com/image.png",
                    "description": "BlaBlaBla....",
                    "tags": ["python", "fastapi"],
                    "location": "Google Meet"
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