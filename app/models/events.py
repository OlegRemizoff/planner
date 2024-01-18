from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.dialects.postgresql import JSONB
from pydantic import BaseModel, Field
from typing import List
from datetime import date

from app.database.conections import Base





class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id")) 
    title = Column(String, nullable=False)
    image = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(JSONB)
    location = Column(String, nullable=False)
    date_to = Column(Date, nullable=False) 




class SEvent(BaseModel):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    title: str 
    image: str 
    description: str
    tags: List[str]
    location: str
    date_to: date



    model_config = {
        "json_schema_extra": {
            "examples": [
                {   "user_id": 0,
                    "title": "FastAPI framework",
                    "image": "https://linktomyimage.com/image.png",
                    "description": "Text",
                    "tags": ["python", "fastapi"],
                    "location": "Orel, Russia",
                    "date_to": date.today().isoformat()
                }
            ],
        }
    }