from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data) # sqlite3 doesn't support .returning(self.model.id)
        res = await self.session.execute(stmt)
        # return res.scalar_one()
        return 'ok'

    async def edit_one(self, id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=id) # sqlite3 doesn't support .returning(self.model.id)
        res = await self.session.execute(stmt)
        # return res.scalar_one()
        return 'ok'
    
    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def find_all_by(self, **filters: dict):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def find_one(self, **filters: dict):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.execute(stmt)
        res = res.scalar_one_or_none()

        if res:
            res = res.to_read_model()
            
        return res

    async def delete_one(self, **filters: dict) -> int:
        stmt = delete(self.model).filter_by(**filters) # sqlite3 doesn't support .returning(self.model.id)
        res = await self.session.execute(stmt)
        # return res.scalar_one()
        return 'ok'
