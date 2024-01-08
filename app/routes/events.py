from fastapi import APIRouter

from app.models.events import SEvent
from app.dao.planner_dao import EventDAO

router = APIRouter(
    prefix="/event",
    tags=["Events"]
)



# Получение всех событий
@router.get("/")
async def retrive_all_events() -> list[SEvent]:
    return await EventDAO.get_find_all()
    

# Получение события по id
@router.get("/{id}")
async def retrive_event(id: int) -> SEvent:
    return await EventDAO.find_by_id(id)


# Создание нового события
@router.post("/new")
async def create_event(data: SEvent) -> None:
    return await EventDAO.add(data)

    
# Удаление события
@router.delete("/delete{id}")
async def delete_event(id: int) -> None:
    return await EventDAO.delete_by_id(id)



   
   
   
   
   
   
   








