import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI

async def get_lang(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    userid = str(userid)
    data = (userid,)
    cur.execute('SELECT * FROM users WHERE id = %s',data)
    user = cur.fetchone()
    lang = user[2]
    base.commit()
    cur.close()
    base.close()
    
    return lang