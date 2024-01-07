from app.database.conections import async_session_maker
from app.models.events import Event, SEvent
from sqlalchemy import select, insert


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalars().one_or_none()



    @classmethod
    async def get_find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
    

        
        

class EventDAO(BaseDAO):
    model = Event

    @classmethod
    async def add(cls, data: SEvent):
        
        new_event = insert(Event).values(
            title=data.title,
            image=data.image,
            description=data.description,
            tags=data.tags,
            location=data.location
        )

        async with async_session_maker() as session:
            await session.execute(new_event)
            await session.commit()
