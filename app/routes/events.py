from fastapi import APIRouter, Depends

from app.models.events import SEvent
from app.models.users import Users
from app.dao.planner_dao import EventDAO
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/event",
    tags=["Events"]
)


        # async with async_session_maker() as session:
        #     query = select(Event).filter_by(user_id=user.id)
        #     result = await session.execute(query)
        #     return result.scalars().all()


# Получение всех событий
@router.get("/")
async def retrive_all_events(user: Users = Depends(get_current_user)) -> list[SEvent]:
    return await EventDAO.get_find_all(user_id=user.id)
    

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