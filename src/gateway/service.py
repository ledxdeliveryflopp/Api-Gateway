from dataclasses import dataclass
from src.gateway.repository import TokenVerifyRepository


@dataclass(repr=False, eq=False)
class TokenVerifyService:
    """Класс сервиса проверки токенов"""
    token_verify_repository: TokenVerifyRepository

    async def verify_token(self):
        return await self.token_verify_repository.verify_token()

    async def verify_token_payload_role(self):
        return await self.token_verify_repository.get_token_payload_role()
