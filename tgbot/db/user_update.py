import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI



# start bd/ connect and create if does'nt exists
async def reg_user(userid, name,lang,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, name,lang,phone,{})
    cur.execute('INSERT INTO users (id, name,lang,phone,acccepted)  VALUES (%s,%s,%s,%s,%s)', data)
    
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
    
async def update_action(userid,action):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (action, str(userid))
    cur.execute('UPDATE users SET action = %s WHERE id = %s', data)
    
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
    
async def update_accepted(userid,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (str(postid), str(userid))
    cur.execute('UPDATE users SET acccepted = array_append(users.acccepted, %s) where id = %s;', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_accepted(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (str(userid),)
    cur.execute("UPDATE users set acccepted = '{}' where id = %s", data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_home(amountbed,timeforlive,pets,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (amountbed,timeforlive,pets,comment,postid)
    print(data)
    cur.execute('UPDATE postshome set amountbed = %s, timeforlive = %s, pets = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_food(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE postsfood set food = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
     
async def reduct_post_medical_care(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE postsmed set helptype = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_clothes(clotype,closize,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (clotype,closize,comment,postid)
    cur.execute('UPDATE postsclothes set clotype = %s,closize = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_first_help(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE postsfirsthelp set helptype = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_kids(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE postskids set helptype = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_other(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE postsother set helptype = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_pets(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE postspets set helptype = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_psy(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE postspsyhologyk set helptype = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def reduct_post_transport(helptype,comment,postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (helptype,comment,postid)
    cur.execute('UPDATE poststransport set way = %s, comment = %s where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
# 
# 
# 

async def delete_post_home(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    print(data)
    cur.execute('DELETE FROM postshome where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_food(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postsfood where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
     
async def delete_post_medical_care(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postsmed where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_clothes(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postsclothes where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_first_help(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postsfirsthelp where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_kids(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postskids where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_other(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postsother where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_pets(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postspets where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_psy(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM postspsyhologyk where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def delete_post_transport(postid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (postid,)
    cur.execute('DELETE FROM poststransport where id = %s', data)
    
    base.commit()
    cur.close()
    base.close()
     