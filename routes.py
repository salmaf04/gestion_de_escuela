from fastapi import APIRouter
from schemas import UserCreateModel

app = APIRouter()

@app.post("/signup")
async def create_user_account(user_input: UserCreateModel) :
    return None