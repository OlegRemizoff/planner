from pydantic import BaseModel
from typing import List, Optional


class Event(BaseModel):
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





