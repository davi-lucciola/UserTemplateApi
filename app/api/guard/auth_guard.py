from dataclasses import dataclass
from fastapi import Depends, Security
from fastapi.security import HTTPAuthorizationCredentials
from app.api.guard import SECURITY_BEARER
from app.domain.models import Token
from app.domain.services import AuthService


@dataclass
class AuthGuard:
    async def __call__(self, 
        auth_service: AuthService = Depends(AuthService),
        auth: HTTPAuthorizationCredentials = Security(SECURITY_BEARER)
    ) -> Token:
        return await auth_service.authenticate(auth)
    
    def __hash__(self) -> int:
        return hash((type(self),))