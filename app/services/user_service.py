from app.config.database import get_db_connection
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.user_model import Item, ItemCreate, ItemDataLogin, ItemLogin
from dotenv import load_dotenv
import os
from datetime import datetime

datenow = datetime.now()
timestamp = datetime.timestamp(datenow)

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
connection = get_db_connection()

async def root():
    return {"message": "User Root"}

async def userlists():
    with connection.cursor() as cursor:
        query = '''
            SELECT
            id,
            PGP_SYM_DECRYPT(username::bytea, %s) AS username,
            PGP_SYM_DECRYPT(email::bytea, %s) AS email,
            PGP_SYM_DECRYPT(address::bytea, %s) AS address,
            PGP_SYM_DECRYPT(phone_number::bytea, %s) AS  phone_number
            FROM users'''
        values = (secret_key, secret_key, secret_key, secret_key)
        cursor.execute(query, values)
        result = cursor.fetchall()
    
    items = [Item(id=row[0], username=row[1], email=row[2], address=row[3], phone_number=row[4]) for row in result]
    result = jsonable_encoder(items)
    
    if not result : 
           return JSONResponse(content={"status": "gagal", "message": "Tidak Terdapat User"}, status_code=404)
    
    return JSONResponse(content={"status" : "berhasil", "data" : result}, status_code=200)


async def createuser(item: ItemCreate):
    with connection.cursor() as cursor:
        query = '''
        INSERT INTO users (username, email, password, address, phone_number) 
        VALUES (
            PGP_SYM_ENCRYPT(%s, %s),
            PGP_SYM_ENCRYPT(%s, %s),
            PGP_SYM_ENCRYPT(%s, %s),
            PGP_SYM_ENCRYPT(%s, %s),
            PGP_SYM_ENCRYPT(%s, %s)
        )'''
        values = (item.username, secret_key,
                  item.email, secret_key,
                  item.password, secret_key,
                  item.address, secret_key,
                  item.phone_number, secret_key)
        try :
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Menambahkan User"}, status_code=201)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)

async def edituser(id: str, item: ItemCreate):
    with connection.cursor() as cursor:
        query = '''UPDATE users 
                SET 
                username = PGP_SYM_ENCRYPT(%s, %s), 
                email =  PGP_SYM_ENCRYPT(%s, %s), 
                password = PGP_SYM_ENCRYPT(%s, %s), 
                address = PGP_SYM_ENCRYPT(%s, %s), 
                phone_number = PGP_SYM_ENCRYPT(%s, %s)
                WHERE 
                id = %s'''
        values = (
            item.username, secret_key,
            item.email, secret_key,
            item.password, secret_key,
            item.address, secret_key,
            item.phone_number, secret_key,
            id)
        try :
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Mengedit User"}, status_code=200)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)

async def deleteuser(id: str):
    with connection.cursor() as cursor:
        query = "DELETE FROM users WHERE id = %s"
        values = (id,)
        try :
            cursor.execute(query, values)
            connection.commit()
            return JSONResponse(content={"status": "success", "message": "Berhasil Menghapus User"}, status_code=200)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)

async def loginuser(item: ItemLogin):
    with connection.cursor() as cursor:
        query = '''
            SELECT 
            PGP_SYM_DECRYPT(u.username::bytea, %s) as username,
            PGP_SYM_DECRYPT(r.role_name::bytea, %s) as role_name
            FROM users u
            join permissions p 
            on u.id = p.user_id
            join roles r 
            on p.role_id = r.id
            WHERE PGP_SYM_DECRYPT(u.username::bytea, %s) = %s AND PGP_SYM_DECRYPT(u.password::bytea, %s) = %s '''
        values = (secret_key, secret_key, secret_key, item.username, secret_key, item.password)

        try :
            cursor.execute(query, values)
            connection.commit()
            result = cursor.fetchone()
            
            if result :
                items = ItemDataLogin(username=result[0], role_name=result[1])
                result = jsonable_encoder(items)

            if result is None :
                querylogin = '''INSERT INTO log_access (username, status, login_date) VALUES (%s, %s, %s)'''
                valueslogin = (item.username, 'Gagal Login',datenow)
                cursor.execute(querylogin, valueslogin)
                connection.commit()
                return JSONResponse(content={"status": "gagal", "message": "Invalid Username or Password, atau akun belum terverifikasi"}, status_code=400)
            
            querylogin = '''INSERT INTO log_access (username, status, login_date) VALUES (%s, %s, %s)'''
            valueslogin = (item.username, 'Berhasil Login',datenow)
            cursor.execute(querylogin, valueslogin)
            connection.commit()
            
            return JSONResponse(content={"status": "success", "message": "Berhasil Login", "data" : result}, status_code=200)
        except Exception as error:
            connection.rollback()
            return JSONResponse(content={"status": "gagal", "message" : str(error)}, status_code=500)

async def userbyid(id: str):
    with connection.cursor() as cursor:
        query = '''
            SELECT
            id,
            PGP_SYM_DECRYPT(username::bytea, %s) AS username,
            PGP_SYM_DECRYPT(email::bytea, %s) AS email,
            PGP_SYM_DECRYPT(address::bytea, %s) AS address,
            PGP_SYM_DECRYPT(phone_number::bytea, %s) AS  phone_number
            FROM users WHERE id = %s'''
        values = (secret_key, secret_key, secret_key, secret_key, id)
        cursor.execute(query, values)
        result = cursor.fetchone()
    
    if result :
        items = Item(id=result[0], username=result[1], email=result[2], address=result[3], phone_number=result[4])
        result = jsonable_encoder(items)
    
    if not result : 
           return JSONResponse(content={"status": "gagal", "message": "Tidak Terdapat User"}, status_code=404)
    
    return JSONResponse(content={"status" : "berhasil", "data" : result}, status_code=200)

       