from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message
from tgbot.keyboards.inline.lang import lang
from tgbot.keyboards.inline.posts import posts_buttons
from tgbot.keyboards.inline.type import type_en, type_ru, type_uk
from tgbot.keyboards.inline.helpBut import help_buttons
from tgbot.misc.texts import regions, make_post, showPost, editPost
from tgbot.keyboards.text_but.region import choice_region
from tgbot.keyboards.text_but.edit_post_but import choice_edit_action
from tgbot.keyboards.text_but.bool_answer import bool_answer
from tgbot.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
import aiogram.types.location
from tgbot.db import user_update
from tgbot.db import posts_db
from tgbot.misc.auf_status import auf_status
from tgbot.misc.get_lang import get_lang
from tgbot.misc.get_post import get_post, get_acccepted, get_post_edit
from tgbot.misc.get_action import get_action
from tgbot.misc.get_type import get_type
from tgbot.db import user_update
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from tgbot.misc.states import MakePost, redactPost
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.content_types import ContentTypesFilter
import random
from aiogram.types import FSInputFile

    
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

edit_post_router = Router()

@edit_post_router.callback_query(lambda c: c.data == 'edit post')
async def edit_post(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    posts = get_post_edit(userid)
    user = get_acccepted(userid)
    p = False
    if answer == 'home':
        for post in posts:
            if str(userid) == str(post[1]):
                photo = FSInputFile('tgbot/img/posts_home/'+ str(post[1]) + str(post[8]) + '.jpg')
                await bot.send_photo(userid, photo, caption= f'id:{post[0]}\n{showPost[language][0]} {post[4]}\n{showPost[language][1]} {post[5]}\n{showPost[language][2]} {post[6]}\n{showPost[language][3]} {post[7]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'food':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'medical care':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'transport':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'kids products':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'products for pets':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'clothes':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}\n{post[6]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'essentials':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'psychological help':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    elif answer == 'other':
        for post in posts:
            if str(userid) == str(post[1]):
                await bot.send_message(userid, f'id:{post[0]}\n{post[4]}\n{post[5]}', reply_markup=types.ReplyKeyboardRemove())
                p = True
            
    if p == False:
        await bot.send_message(userid,'Not Found')
    else:
        but = choice_edit_action(language)
        await bot.send_message(userid,editPost[language][1], reply_markup=but.as_markup(resize_keyboard=True)) 
        await state.set_state(redactPost.act)  

@edit_post_router.message( state = redactPost.act)
async def get_act(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    language = await get_lang(userid)
    answer = get_action(userid)
    
    if message.text == 'Delete' or message.text == 'Удалить' or message.text == 'Видалити':
        await state.set_state(redactPost.postid2)
        await bot.send_message(userid,editPost[language][0], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_message(userid,editPost[language][0], reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(redactPost.postid)

@edit_post_router.message( state = redactPost.postid2)
async def get_postid2(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    language = await get_lang(userid)
    answer = get_action(userid)
    postid2 = message.text
    help_but = help_buttons(language)
    await state.update_data(postid2=postid2)
    if answer == 'home':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_home(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'food':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_food(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'medical care':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_medical_care(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'clothes':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_clothes(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'essentials':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_first_help(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'kids products':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_kids(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'other':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_other(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'products for pets':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_pets(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'psychological help':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_psy(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()
    elif answer == 'transport':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.delete_post_transport(postid2)
        await bot.send_message(userid,editPost[language][2], reply_markup=help_but.as_markup()) 
        await state.clear()

@edit_post_router.message( state = redactPost.postid)
async def get_postid(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    type_user = get_type(userid)
    await state.update_data(postid=message.text)
    if answer == 'home':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][1],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.amountbed)
        else:
            await bot.send_message(userid,make_post[language][11],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.amountbed)
    elif answer == 'food':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'medical care':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'essentials':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'psychological help':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'kids products':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'transport':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'products for pets':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'other':
        if type_user == 'volounter':
            await bot.send_message(userid,make_post[language][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
        else:
            await bot.send_message(userid,make_post[language][14],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(redactPost.helptype)
    elif answer == 'clothes':
        await bot.send_message(userid,make_post[language][9],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(redactPost.clotype)
        
        
@edit_post_router.message(state = redactPost.clotype)
async def get_clotype(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    await state.update_data(clotype=message.text)
    await state.set_state(redactPost.closize)
    await bot.send_message(userid,make_post[language][10],reply_markup=types.ReplyKeyboardRemove())
    
@edit_post_router.message(state = redactPost.closize)
async def get_closize(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    await state.update_data(closize=message.text)
    await state.set_state(redactPost.comment)
    await bot.send_message(userid,make_post[language][6],reply_markup=types.ReplyKeyboardRemove())
    
@edit_post_router.message(state = redactPost.helptype)
async def get_closize(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    await state.update_data(helptype=message.text)
    await state.set_state(redactPost.comment)
    await bot.send_message(userid,make_post[language][6],reply_markup=types.ReplyKeyboardRemove())
        
@edit_post_router.message(state = redactPost.amountbed)
async def get_amount_bed(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    type_user = get_type(userid)
    answer = get_action(userid)
    language = await get_lang(userid)
    try:
        await state.update_data(amountbed=int(message.text))
    except:
        await bot.send_message(userid,make_post[language][2],reply_markup=types.ReplyKeyboardRemove())
        return
    await state.set_state(redactPost.time_for_live)
    if type_user == 'volounter':
        await bot.send_message(userid,make_post[language][3],reply_markup=types.ReplyKeyboardRemove())    
    else:
        await bot.send_message(userid,make_post[language][12],reply_markup=types.ReplyKeyboardRemove())    
    
@edit_post_router.message(state = redactPost.time_for_live)
async def get_time(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    type_user = get_type(userid)
    language = await get_lang(userid)
    await state.update_data(time_for_live=message.text)
    bool_answers = bool_answer(lang)
    if type_user == 'volounter':
        await bot.send_message(userid,make_post[language][4],reply_markup=bool_answers.as_markup(resize_keyboard=True))
    else:
        await bot.send_message(userid,make_post[language][13],reply_markup=bool_answers.as_markup(resize_keyboard=True))
    await state.set_state(redactPost.pets)
    
       
    
@edit_post_router.message(state = redactPost.pets)
async def get_pets(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    if message.text == 'Да':
        answ = True
    else:
        answ = False
    await state.update_data(pets=answ)
    await bot.send_message(userid,make_post[language][5],reply_markup=types.ReplyKeyboardRemove())
    print(make_post[lang][5])
    await state.set_state(redactPost.comment) 
    
@edit_post_router.message(state = redactPost.comment)
async def get_comment(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    language = await get_lang(userid)
    await state.update_data(comment = message.text)
    if answer == 'home':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_home(user_data['amountbed'],user_data['time_for_live'],user_data['pets'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'food':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_food(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'medical care':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_medical_care(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'clothes':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_clothes(user_data['clotype'],user_data['closize'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'essentials':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_first_help(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'kids products':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_kids(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'other':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_other(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'products for pets':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_pets(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'psychological help':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_psy(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'transport':
        type = get_type(userid)
        user_data = await state.get_data()
        await user_update.reduct_post_transport(user_data['helptype'],user_data['comment'],user_data['postid'])
        await bot.send_message(userid,make_post[language][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()  
    
    
