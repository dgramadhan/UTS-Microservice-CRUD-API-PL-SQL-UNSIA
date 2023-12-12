from fastapi import FastAPI
from app.routes import users, roles, permission
from app.config.database import get_db_connection

connection = get_db_connection()
app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(roles.router, prefix="/roles", tags=["roles"])
app.include_router(permission.router, prefix="/permissions", tags=["permissions"])

@app.on_event("startup")
async def up_db():
    print("Database Connected")

@app.on_event("shutdown")
async def down_db():
    connection.close()

@app.get("/")
async def root():
    return {"message": "Server Sedang Berjalan"}