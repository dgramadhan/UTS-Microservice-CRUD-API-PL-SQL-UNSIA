from sqlalchemy import values
from app.config.database import get_db_connection
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.permissions_model import Permission, PermissionCreate, PermissionEdit
from dotenv import load_dotenv
import os

connection = get_db_connection()
load_dotenv()
secret_key = os.getenv('SECRET_KEY')

async def root():
    return {"message" : "Permission Root"}

async def createpermission(item: PermissionCreate):
    with connection.cursor() as cursor:
        query = '''
            INSERT INTO permissions (user_id, role_id)
            VALUES (
                %s, %s
        )
        '''
        values = (item.user_id, item.role_id)

        try:
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Menambahkan Permission"}, status_code=201)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)
        
async def editpermission(id:str, item: PermissionEdit):
    with connection.cursor() as cursor:
        query = '''
            UPDATE permissions SET
            role_id = %s
            WHERE
            id = %s
        '''
        values = (
            item.role_id, id
        )
        try :
            ressult = cursor.execute(query, values)
            print(ressult)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Mengedit Permission"}, status_code=200)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)
        
async def listpermissions():
    with connection.cursor() as cursor:
        query = '''
            SELECT
            p.id,
            p.user_id,
            p.role_id,
            PGP_SYM_DECRYPT(u.username::bytea, %s) AS username,
            PGP_SYM_DECRYPT(r.role_name::bytea, %s) AS role_name  
            FROM permissions p
            join users u
            on p.user_id = u.id
            join roles r
            on p.role_id = r.id'''
        values = (secret_key,secret_key)
        
        try :
            cursor.execute(query, values)
            res  = cursor.fetchall()

            items = [Permission(id=row[0], user_id=row[1], role_id=row[2],username=row[3], role_name=row[4]) for row in res]
            result = jsonable_encoder(items)

            if not result : 
                return JSONResponse(content={"status": "gagal", "message": "Tidak Terdapat Permission"}, status_code=404)
            return JSONResponse(content={"status" : "berhasil", "data" : result}, status_code=200)
        except Exception as error:
                connection.rollback()
                return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)
   

   
    
   

async def deletepermissions(id: str):
    with connection.cursor() as cursor:
        query = "DELETE FROM permissions WHERE id = %s"
        values = (id,)
        try :
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Menghapus Permission"}, status_code=200)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)