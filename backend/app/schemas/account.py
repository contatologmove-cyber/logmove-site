from pydantic import BaseModel, EmailStr


class AccountCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class AccountResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    active: bool

    class Config:
        from_attributes = True