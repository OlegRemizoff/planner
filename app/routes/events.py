from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select
from typing import List

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


# Обновление события
@router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if not event: 
        raise HTTPException(
            status_code=status. HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    event_data = new_data.dict(exclude_unset=True)
    for key, value in event_data.items():
        setattr(event, key, value)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


# Удаление события
@router.delete("/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if not event: 
        raise HTTPException(
            status_code=status. HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    
    session.delete(event)
    session.commit()
    return {"message": "Event deleted successfully"}

# Удалить все события
@router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "Events deleted successfully"}