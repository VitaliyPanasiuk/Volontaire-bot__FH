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
    cur.execute('''CREATE TABLE IF NOT EXISTS postsHome(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        amountbed text,
        timeforlive text,
        pets boolean,
        comment text,
        img text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsFood(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        food text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsMed(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsTransport(
        id serial primary key,
        userid text references users(id),
        type text,
        way text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsKids(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsPets(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsClothes(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        clotype text,
        closize text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsFirsthelp(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsPsyhologyk(
        id serial primary key,
        userid text references users(id),
        type text,
        geo text,
        helptype text,
        comment text,
        phone text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS postsOther(
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
     
