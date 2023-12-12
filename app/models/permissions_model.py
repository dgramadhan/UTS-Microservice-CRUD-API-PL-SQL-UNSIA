from pydantic import BaseModel

class Permission(BaseModel):
    id: int
    user_id: int
    role_id: int
    username: str
    role_name: str

class PermissionCreate(BaseModel):
    user_id: int
    role_id: int

class PermissionEdit(BaseModel):
    role_id: int