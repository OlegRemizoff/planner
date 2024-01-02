from fastapi import APIRouter, Request, HTTPException, Depends, Body, status
from sqlalchemy import select, delete, insert, func, and_, or_
from typing import List, Tuple

from app.models.events import Event, EventUpdate
from app.database.conections import get_session # маршруты смогут получить доступ к созданному объекту сеанса


router = APIRouter(
    prefix="/event",
    tags=["Events"]
)

events = []


# Получение всех событий
@router.get("/", response_model=List[Event]) 
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).scalars().all() # метод возвращает список значений, а не объекты моделей
    return events


# Получение события по id
@router.get("/{id}", response_model=Event)
async def retrive_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if not event: 
        raise HTTPException(
            status_code=status. HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event

# Создание нового события
@router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
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