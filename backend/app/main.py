from fastapi import FastAPI

from app.database import engine, Base
from app.models.account import Account
from app.routers.accounts import router as accounts_router
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LogMove API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "empresa": "LogMove",
        "status": "online"
    }

app.include_router(accounts_router)