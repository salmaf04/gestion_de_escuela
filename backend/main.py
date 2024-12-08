from fastapi import FastAPI
from .presentation.routes.auth import router as auth_router
from .presentation.routes.administrador import router as admin_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(admin_router)
