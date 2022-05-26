import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI
from tgbot.misc.get_action import get_action
from tgbot.misc.get_type import get_type

def get_post(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    userid = str(userid)
    action = get_action(userid)
    types = str(get_type(userid))
    if types == 'volunteer':
        types = 'needy'
    elif types == 'needy':
        types = 'volunteer'
    if action == 'home':
        action_name = 'postshome'
    elif action == 'food':
        action_name = 'postsfood'
    elif action == 'medical care':
        action_name = 'postsmed'
    elif action == 'transport':
        action_name = 'poststransport'
    elif action == 'kids products':
        action_name = 'postskids'
    elif action == 'products for pets':
        action_name = 'postspets'
    elif action == 'clothes':
        action_name = 'postsclothes'
    elif action == 'essentials':
        action_name = 'postsfirsthelp'
    elif action == 'psychological help':
        action_name = 'postspsyhologyk'
    elif action == 'other':
        action_name = 'postsother'
    cur.execute(sql.SQL('''SELECT * FROM {table} WHERE type = %s''').format(table = sql.Identifier(action_name)),(types,))
    posts = cur.fetchall()
    
    base.commit()
    cur.close()
    base.close()
    
    return posts

def get_post_edit(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    userid = str(userid)
    action = get_action(userid)
    types = str(get_type(userid))
    if action == 'home':
        action_name = 'postshome'
    elif action == 'food':
        action_name = 'postsfood'
    elif action == 'medical care':
        action_name = 'postsmed'
    elif action == 'transport':
        action_name = 'poststransport'
    elif action == 'kids products':
        action_name = 'postskids'
    elif action == 'products for pets':
        action_name = 'postspets'
    elif action == 'clothes':
        action_name = 'postsclothes'
    elif action == 'essentials':
        action_name = 'postsfirsthelp'
    elif action == 'psychological help':
        action_name = 'postspsyhologyk'
    elif action == 'other':
        action_name = 'postsother'
    cur.execute(sql.SQL('''SELECT * FROM {table} WHERE type = %s''').format(table = sql.Identifier(action_name)),(types,))
    posts = cur.fetchall()
    
    base.commit()
    cur.close()
    base.close()
    
    return posts

def get_acccepted(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    userid = str(userid)
    action = get_action(userid)
    types = str(get_type(userid))
    data = (action,userid)
    cur.execute(sql.SQL('''SELECT * FROM users WHERE id = %s'''),(userid,))
    user = cur.fetchall()
    print(user)
    base.commit()
    cur.close()
    base.close()
    
    return user