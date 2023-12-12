from fastapi import APIRouter
from app.services.user_service import createuser, deleteuser, edituser, loginuser, userbyid, userlists, root
from app.models.user_model import ItemCreate, ItemLogin

router = APIRouter()

@router.get("/")
async def get_root():
    return await root()

@router.get("/list")
async def get_list_users():
    return await userlists()

@router.post("/add")
async def create_user(item: ItemCreate):
    return await createuser(item)

@router.put("/edit/{user_id}")
async def edit_user(user_id: str, item: ItemCreate):
    return await edituser(user_id, item)

@router.delete("/delete/{user_id}")
async def delete_user(user_id: str):
    return await deleteuser(user_id)

@router.post("/login")
async def login_user(item: ItemLogin):
    return await loginuser(item)

@router.get("/{user_id}")
async def user_by_id(user_id: str):
    return await userbyid(user_id)