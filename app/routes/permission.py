from turtle import st
from fastapi import APIRouter
from app.models.permissions_model import PermissionCreate, PermissionEdit
from app.services.permission_service import createpermission, deletepermissions, editpermission, listpermissions, root

router = APIRouter()

@router.get("/")
async def get_root():
    return await root()

@router.post("/add")
async def create_permission(item: PermissionCreate):
    return await createpermission(item)

@router.put("/edit/{id_permission}")
async def edit_permission(id_permission: str, item: PermissionEdit):
    return await editpermission(id_permission, item)

@router.get("/list")
async def list_permissions():
    return await listpermissions()

@router.delete("/delete/{id_permission}")
async def delete_permission(id_permission: str):
    return await deletepermissions(id_permission)