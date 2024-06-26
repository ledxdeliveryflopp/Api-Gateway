from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.settings.db import async_session
from src.settings.repository import SessionRepository
from src.settings.service import SessionService


async def get_session():
    async with async_session() as session:
        yield session


async def get_session_service(session: AsyncSession = Depends(get_session)):
    session_service = SessionService(session_repository=SessionRepository(session=session))
    return session_service
