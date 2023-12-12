from pydantic import BaseModel

class Item(BaseModel):
    id: int
    username: str
    email: str
    address: str
    phone_number: str

class ItemCreate(BaseModel):
    username: str
    password: str
    email: str
    address: str
    phone_number: str

class ItemLogin(BaseModel):
    username: str
    password: str

class ItemDataLogin(BaseModel):
    username: str
    role_name: str