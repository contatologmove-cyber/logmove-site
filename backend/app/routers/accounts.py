from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.account import AccountCreate, AccountResponse
from app.services.account_service import create_account

router = APIRouter(
    prefix="/api/v1/accounts",
    tags=["Accounts"]
)


@router.post("/", response_model=AccountResponse)
def register(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account)