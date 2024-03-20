from dataclasses import dataclass
from src.settings.repository import SessionRepository


@dataclass
class SessionService:
    session_repository: SessionRepository

    async def create_object(self, save_object: dict):
        data = await self.session_repository.session_add(save_object=save_object)
        return data

    async def delete_object(self, delete_object: dict):
        data = await self.session_repository.session_delete(delete_object=delete_object)
        return data
