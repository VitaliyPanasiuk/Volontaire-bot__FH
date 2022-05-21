import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI



# start bd/ connect and create if does'nt exists
async def postgre_start():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    if base:
        print('data base connect Ok!')
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id text primary key,
        name text,
        lang text default 'uk', 
        status text,
        action text, 
        phone text, 
        acccepted text[]
        )''')
    cur.execute('CREATE TABLE IF NOT EXISTS postshome(id serial primary key,userid text references users(id),type text,geo text,amountbed text,timeforlive text,pets boolean,comment text,img text,phone text)')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsfood(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        food text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsmed(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS poststransport(
        id serial primary key,
        userid text references users(id),
        type text,
        way text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postskids(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postspets(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsclothes(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        clotype text,
        closize text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsfirsthelp(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postspsyhologyk(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsother(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    
    base.commit()
    cur.close()
    base.close()
     
