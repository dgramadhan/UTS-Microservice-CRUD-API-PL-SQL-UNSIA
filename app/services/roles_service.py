from app.config.database import get_db_connection
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.roles_model import Role, RoleCreate
from dotenv import load_dotenv
import os

connection = get_db_connection()
load_dotenv()
secret_key = os.getenv('SECRET_KEY')

async def root():
    return {"message" : "Role Root"}

async def createrole(item: RoleCreate):
    with connection.cursor() as cursor:
        query = '''
            INSERT INTO roles (role_name, description)
            VALUES (
                PGP_SYM_ENCRYPT(%s, %s), 
                PGP_SYM_ENCRYPT(%s, %s)
            )
        '''
        values = (
            item.role_name, secret_key,
            item.description, secret_key
        )

        try:
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Menambahkan Role"}, status_code=201)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)

async def listroles():
    with connection.cursor() as cursor:
        query = '''
            SELECT
            id,
            PGP_SYM_DECRYPT(role_name::bytea, %s),
            PGP_SYM_DECRYPT(description::bytea, %s)
            FROM roles'''
        values = (secret_key, secret_key)
        cursor.execute(query, values)
        result = cursor.fetchall()
    
    items = [Role(id=row[0], role_name=row[1], description=row[2]) for row in result]
    result = jsonable_encoder(items)

    if not result : 
           return JSONResponse(content={"status": "gagal", "message": "Tidak Terdapat User"}, status_code=404)
    
    return JSONResponse(content={"status" : "berhasil", "data" : result}, status_code=200)

async def rolebyid(role_id: str):
    with connection.cursor() as cursor:
        query = '''
            SELECT
            id,
            PGP_SYM_DECRYPT(role_name::bytea, %s),
            PGP_SYM_DECRYPT(description::bytea, %s)
            FROM roles
            WHERE id = %s'''
        values = (secret_key, secret_key, role_id)
        cursor.execute(query, values)
        result = cursor.fetchone()
    
    if result :
        items = Role(id=result[0], role_name=result[1], description=result[2])
        result = jsonable_encoder(items)
    
    if not result : 
           return JSONResponse(content={"status": "gagal", "message": "Tidak Terdapat Role"}, status_code=404)
    
    return JSONResponse(content={"status" : "berhasil", "data" : result}, status_code=200)


async def editrole(id: str, item: RoleCreate):
    with connection.cursor() as cursor:
        query = '''UPDATE roles 
                SET 
                role_name = PGP_SYM_ENCRYPT(%s, %s), 
                description = PGP_SYM_ENCRYPT(%s, %s)
                WHERE id = %s'''
        values = (item.role_name, secret_key, item.description, secret_key, id)
        try :
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Mengedit Role"}, status_code=200)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)

async def deleterole(id: str):
    with connection.cursor() as cursor:
        query = "DELETE FROM roles WHERE id = %s"
        values = (id,)
        try :
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Menghapus Roles"}, status_code=200)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)
