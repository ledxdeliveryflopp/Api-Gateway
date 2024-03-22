from dataclasses import dataclass
from datetime import datetime

from fastapi import HTTPException
from jose import jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request
from src.gateway.models import TokenModel
from src.settings.service import SessionService
from src.settings.settings import settings


@dataclass(repr=False, eq=False)
class TokenVerifyRepository:
    """Класс для взаимодействия с БД для токенов"""
    session: AsyncSession
    session_service: SessionService
    request: Request

    async def find_token(self, jwt_token: str):
        """Поиск токена"""
        token = await self.session.execute(select(TokenModel).filter(TokenModel.token == jwt_token))
        return token.scalar()

    async def verify_token(self):
        """Проверка токена на существование и срок действия"""
        header_token = self.request.headers.get('Authorization')
        header_token = header_token.replace("Bearer ", "")
        token = await self.find_token(jwt_token=header_token)
        if not token:
            raise HTTPException(status_code=403, detail="bad token")
        date = datetime.utcnow()
        if token.expire < date:
            await self.session_service.delete_object(delete_object=token)
            raise HTTPException(status_code=403, detail="bad token")
        return status.HTTP_200_OK

    async def get_token_payload_role(self):
        header_token = self.request.headers.get('Authorization')
        header_token = header_token.replace("Bearer ", "")
        token = await self.find_token(jwt_token=header_token)
        if not token:
            raise HTTPException(status_code=403, detail="bad token")
        date = datetime.utcnow()
        if token.expire < date:
            await self.session_service.delete_object(delete_object=token)
            raise HTTPException(status_code=403, detail="bad token")
        token_data = token.token
        token_payload = jwt.decode(token=token_data, key=settings.jwt_settings.jwt_secret,
                                   algorithms=settings.jwt_settings.jwt_algorithm)
        user_role = token_payload.get("user_role")
        if user_role == "user":
            raise HTTPException(status_code=403, detail="bad token role")
        return status.HTTP_200_OK

