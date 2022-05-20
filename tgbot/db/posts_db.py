import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI



# start bd/ connect and create if does'nt exists
async def make_post_home(userid, type, geo,amountbed,timeforlive,pets,comment,img,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,amountbed,timeforlive,pets,comment,img,phone,)
    print(data)
    cur.execute('INSERT INTO postshome (userid, type, geo,amountbed,timeforlive,pets,comment,img,phone)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_food(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO postsfood (userid, type, geo,food,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
     
async def make_post_medical_care(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO postsmed (userid, type, geo,helptype,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_clothes(userid, type, geo,clotype,closize,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,clotype,closize,comment,phone)
    cur.execute('INSERT INTO postclothes (userid, type, geo,clotype,closize,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_first_help(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO postsfirsthelp (userid, type, geo,helptype,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_kids(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO postskids (userid, type, geo,helptype,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_other(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO postsother (userid, type, geo,helptype,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_pets(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO postspets (userid, type, geo,helptype,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_psy(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO postspsyhologyk (userid, type, geo,helptype,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def make_post_transport(userid, type, geo,helptype,comment,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, geo,helptype,comment,phone)
    cur.execute('INSERT INTO poststransport (userid, type, geo,way,comment,phone)  VALUES (%s,%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
     
     