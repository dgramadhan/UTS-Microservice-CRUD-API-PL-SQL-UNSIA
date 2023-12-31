from pydantic import BaseModel

class Role(BaseModel):
    id: int
    role_name: str
    description: str

class RoleCreate(BaseModel):
    role_name: str
    description: str