from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountCreate
from app.core.security import hash_password

def create_account(db: Session, account: AccountCreate):

    new_account = Account(
        name=account.name,
        email=account.email,
        phone=account.phone,
       password_hash=hash_password(account.password),  # depois vamos criptografar
        active=True
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account