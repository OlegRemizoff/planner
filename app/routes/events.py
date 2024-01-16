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
async def create_event(data: SEvent) -> dict:
    return await EventDAO.add_event(data)


# Обновление события
@router.put("/{id}")
async def update_event(id: int, new_data: SEvent) -> dict:
    return await EventDAO.update_event(id, new_data)
    

# Удаление события
@router.delete("/delete{id}")
async def delete_event(id: int) -> dict:
    return await EventDAO.delete_by_id(id)






   
   

   
   








{
  "title": "updated",
  "image": "https://google.com/image",
  "description": "blablalba",
  "tags": [
    "python"
  ],
  "location": "Russia"
}