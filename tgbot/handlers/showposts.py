from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message
from tgbot.keyboards.inline.lang import lang
from tgbot.keyboards.inline.posts import posts_buttons
from tgbot.keyboards.inline.type import type_en, type_ru, type_uk
from tgbot.keyboards.inline.helpBut import help_buttons
from tgbot.misc.texts import regions, make_post, showPost
from tgbot.keyboards.text_but.region import choice_region
from tgbot.keyboards.text_but.bool_answer import bool_answer
from tgbot.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
import aiogram.types.location
from tgbot.db import user_update
from tgbot.db import posts_db
from tgbot.misc.auf_status import auf_status
from tgbot.misc.get_lang import get_lang
from tgbot.misc.get_post import get_post, get_acccepted
from tgbot.misc.get_action import get_action
from tgbot.misc.get_type import get_type
from tgbot.db import user_update
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from tgbot.misc.states import MakePost
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.content_types import ContentTypesFilter
import random
from aiogram.types import FSInputFile

    
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

show_posts_router = Router()

@show_posts_router.callback_query(lambda c: c.data == 'show posts')
async def show_posts(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    posts = get_post(userid)
    user = get_acccepted(userid)
    post_but = posts_buttons(language)
    if answer == 'home':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                photo = FSInputFile('tgbot/img/posts_home/'+ str(post[1]) + str(post[8]) + '.jpg')
                await bot.send_photo(userid, photo, caption= f'{showPost[language][0]} {post[4]}\n{showPost[language][1]} {post[5]}\n{showPost[language][2]} {post[6]}\n{showPost[language][3]} {post[7]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'food':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'medical care':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'transport':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'kids products':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'products for pets':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'clothes':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}\n{post[6]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'essentials':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'psychological help':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'other':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
        
@show_posts_router.callback_query(lambda c: c.data == 'confirm_post')
async def confirm_post(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    language = await get_lang(userid)
    user = get_acccepted(userid)
    posts = get_post(userid)
    accepted = user[0][4]
    for i in posts:
        if str(accepted[-1]) == str(i[0]):
            await bot.send_message(userid,f'Phone: {i[9]}')

@show_posts_router.callback_query(lambda c: c.data == 'reject_post')
async def confirm_post(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    language = await get_lang(userid)
    user = get_acccepted(userid)
    posts = get_post(userid)
    post_but = posts_buttons(language)
    answer = get_action(userid)
    if answer == 'home':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                photo = FSInputFile('tgbot/img/posts_home/'+ str(post[1]) + str(post[8]) + '.jpg')
                await bot.send_photo(userid, photo, caption= f'{showPost[language][0]} {post[4]}\n{showPost[language][1]} {post[5]}\n{showPost[language][2]} {post[6]}\n{showPost[language][3]} {post[7]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'food':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'medical care':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'transport':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'kids products':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'products for pets':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'clothes':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}\n{post[6]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'essentials':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'psychological help':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)
    elif answer == 'other':
        for post in posts:
            if str(post[0]) not in user[0][4]:
                await bot.send_message(userid, f'{post[4]}\n{post[5]}', reply_markup=post_but.as_markup())
                postid = post[0]
                await user_update.update_accepted(userid,postid)
                break
            await user_update.delete_accepted(userid)

            
    
    
    
