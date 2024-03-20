from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from src.gateway.repository import TokenVerifyRepository
from src.gateway.service import TokenVerifyService
from src.settings.depends import get_session, get_session_service
from src.settings.service import SessionService


async def get_token_verify_service(request: Request, session: AsyncSession = Depends(
                                   get_session), session_service: SessionService = Depends(
                                   get_session_service)):
    token_verify_service = TokenVerifyService(token_verify_repository=TokenVerifyRepository(
        request=request, session=session, session_service=session_service))
    return token_verify_service
