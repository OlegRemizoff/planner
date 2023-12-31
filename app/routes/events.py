from fastapi import APIRouter, Body , HTTPException, status
from typing import List
from app.models.events import Event


router = APIRouter(
    prefix="/event",
    tags=["Events"]
)

events = []


# Получение всех событий
@router.get("/", response_model=List[Event])
async def retrive_all_events() -> List[Event]:
    return events


# Получение события по id
@router.get("/{id}", response_model=Event)
async def retrive_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    
    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

# Создание нового события
@router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {"message": "Event created successfully"}


# Удаление события
@router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return { "message": "Event deleted successfully" }
    
    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


# Удалить все события
@router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "Events deleted successfully"}