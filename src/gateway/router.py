from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from src.gateway.depends import get_token_verify_service
from src.gateway.service import TokenVerifyService

gateway_api_router = APIRouter(
    prefix="/gateway",
    tags=["gateway"],
)

bearer_token = HTTPBearer()


@gateway_api_router.get('/verify-token/')
async def verify_token_router(token_service: TokenVerifyService = Depends(get_token_verify_service),
                              token: str = Depends(bearer_token)):
    """Роутер проверки токена"""
    return await token_service.verify_token()


@gateway_api_router.get('/verify-token-role/')
async def verify_token_role_router(token_service: TokenVerifyService =
                                   Depends(get_token_verify_service),
                                   token: str = Depends(bearer_token)):
    """Роутер проверки прав доступа токена"""
    return await token_service.verify_token_payload_role()
