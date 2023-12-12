from fastapi import APIRouter
from app.models.roles_model import RoleCreate
from app.services.roles_service import createrole, deleterole, editrole, listroles, rolebyid, root

router = APIRouter()

@router.get("/")
async def get_root():
    return await root()

@router.post("/add")
async def create_role(item: RoleCreate):
    return await createrole(item)

@router.get("/list")
async def list_role():
    return await listroles()

@router.get("/{role_id}")
async def role_by_id(role_id: str):
    return await rolebyid(role_id)

@router.put("/edit/{role_id}")
async def edit_role(role_id: str, item: RoleCreate):
    return await editrole(role_id, item)

@router.delete("/delete/{role_id}")
async def delete_role(role_id: str):
    return await deleterole(role_id)