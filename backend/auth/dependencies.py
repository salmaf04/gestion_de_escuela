from fastapi.security import HTTPBearer
from fastapi import Request, status
from utils import decode_token
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials


class AccessTokenBearer(HTTPBearer) :
    
    async def __init__(self, auto_error: bool=True) :
        return super().__init__(auto_error=auto_error)
    
    async def __call__(self , request : Request) -> HTTPAuthorizationCredentials | None :
        creds = super().__call__(request)

        token = creds.credentials

        token_data = decode_token(token)

        if token_data is None :
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid Credentials"
            )
        
        if token_data['refresh'] :
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid Credentials"
            )

        return token_data
        

    