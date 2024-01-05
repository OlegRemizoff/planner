from app.database.conections import async_session_maker
from app.models.events import Event
from sqlalchemy import select


class BaseDAO:
    model = None

    @classmethod
    async def get_find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        

class EventDAO(BaseDAO):
    model = Event