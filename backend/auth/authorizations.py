## authorizations.py
from functools import wraps
from fastapi import HTTPException

def authorize(role: list):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user =  await kwargs.get("current_user")
            user_role = user.type
            if user_role not in role:
                raise HTTPException(status_code=403, detail=f"User is not authorized to access , only avaliable for {role}")
            return await func(*args, **kwargs)
        return wrapper
    return decorator