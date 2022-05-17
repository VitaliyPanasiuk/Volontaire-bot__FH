import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI



# start bd/ connect and create if does'nt exists
async def reg_user(userid, name,lang):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, name,lang)
    cur.execute('INSERT INTO users (id, name,lang)  VALUES (%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
     
     
async def update_status(userid,status):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (status, str(userid))
    cur.execute('UPDATE users SET status = %s WHERE id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def update_lang(userid,lang):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (lang, str(userid))
    cur.execute('UPDATE users SET lang = %s WHERE id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
     