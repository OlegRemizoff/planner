from fastapi import APIRouter, Depends, HTTPException, status, Response
import requests
from app.models.events import SEvent
from app.models.users import Users
from app.dao.planner_dao import EventDAO
from app.dependencies import get_current_user
from app.utils import check_text


router = APIRouter(
    prefix="/event",
    tags=["Events"]
)



# Получение всех событий
@router.get("/")
async def retrive_all_events(user: Users = Depends(get_current_user)) -> list[SEvent]:
    return await EventDAO.get_find_all(user_id=user.id)
    

# Получение события по id
@router.get("/{id}")
async def retrive_event(id: int, user: Users = Depends(get_current_user)) -> SEvent:
    result = await EventDAO.find_one_or_none(id=id, user_id=user.id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return result



# Создание нового события
@router.post("/new")
async def create_event(data: SEvent) -> dict:
    raw_text = str(data.description) # забираем текст из JSON-формы и передаем его в check_text
    correxted_text = await check_text(text=raw_text) 
    print("\x1b[31;1m" + "До     " + "\x1b[0m", data.description)
    print("\x1b[31;1m" + "После  " + "\x1b[0m", correxted_text)
    return Response("Success!")
    # return await EventDAO.add_event(data)


# Обновление события
@router.put("/{id}")
async def update_event(id: int, new_data: SEvent) -> dict:
    return await EventDAO.update_event(id, new_data)
    

# Удаление события
@router.delete("/delete{id}")
async def delete_event(id: int, user: Users = Depends(get_current_user)) -> dict:
    result = await EventDAO.find_one_or_none(id=id, user_id=user.id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
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