from app.database.conections import async_session_maker
from app.models.events import Event, SEvent
from app.models.users import Users
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
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
    

    @classmethod
    async def delete_by_id(cls, model_id: int):
        async with async_session_maker() as session:          
            obj = await session.get(cls.model, model_id)
            if obj:
                await session.delete(obj)
                await session.commit()
                return {"message": "Object has been successefuly deleted"}
            return {"message": "Object not found"}

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            

        
class EventDAO(BaseDAO):
    model = Event

    @classmethod
    async def add_event(cls, data: SEvent):
        
        new_event = insert(cls.model).values(
            title=data.title,
            image=data.image,
            description=data.description,
            tags=data.tags,
            location=data.location,
            user_id=data.user_id,
            date_to=data.date_to
        )

        async with async_session_maker() as session:
            await session.execute(new_event)
            await session.commit()
            return {"message": "Object has been successefuly created"}

    @classmethod
    async def update_event(cls, id: int, new_data: SEvent):
        async with async_session_maker() as session: 
            event = await session.get(cls.model, id)
            if event:
                try:
                    event_data = new_data.dict(exclude_unset=True)
                    for key, value in event_data.items():
                        setattr(event, key, value)
                        session.add(event)
                        await session.commit()
                        await session.refresh(event)
                        return {"message": "Object has been successefuly updated"}
                except:
                    return Exception("Somethin went wrong...")
            return {"message": "Object not found"}
        


class UsersDAO(BaseDAO):
    model = Users
    