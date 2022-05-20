from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message
from tgbot.keyboards.inline.lang import lang
from tgbot.keyboards.inline.type import type_en, type_ru, type_uk
from tgbot.keyboards.inline.helpBut import help_buttons
from tgbot.misc.texts import regions, make_post
from tgbot.keyboards.text_but.region import choice_region
from tgbot.keyboards.text_but.bool_answer import bool_answer
from tgbot.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
import aiogram.types.location
from tgbot.db import user_update
from tgbot.db import posts_db
from tgbot.misc.auf_status import auf_status
from tgbot.misc.get_lang import get_lang
from tgbot.misc.get_action import get_action
from tgbot.misc.get_type import get_type
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from tgbot.misc.states import MakePost
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.content_types import ContentTypesFilter
import random

    
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

make_post_router = Router()


    

    
@make_post_router.callback_query(lambda c: c.data == 'make post')
async def user_start(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    answer = get_action(userid)
    lang = await get_lang(userid)
    if answer == 'home':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'food':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'medical care':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'essentials':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'kids products':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'clothes':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'other':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'psychological help':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'products for pets':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
    elif answer == 'transport':
        region = choice_region(lang)
        await bot.send_message(userid,make_post[lang][0],reply_markup=region.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo)
        
        
@make_post_router.message(content_types=types.ContentType.ANY, state = MakePost.geo)
async def get_geo(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    answer = get_action(userid)
    geo_buttons = ReplyKeyboardBuilder()
    geo_buttons.row(
        types.KeyboardButton(text="Send geo",request_location=True)
    )
    print(message.text)
    if message.text == 'Запросить геолокацию':
        await bot.send_message(userid,'Отправьте геолокацию',reply_markup=geo_buttons.as_markup(resize_keyboard=True))
        await state.set_state(MakePost.geo2)
    else:
        await state.update_data(geo=message.text)
    
        if answer == 'home':
            await bot.send_message(userid,make_post[lang][1],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.amountbed)
        elif answer == 'food':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'medical care':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'essentials':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'psychological help':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'kids products':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'transport':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'products for pets':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'other':
            await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.helptype)
        elif answer == 'clothes':
            await bot.send_message(userid,make_post[lang][9],reply_markup=types.ReplyKeyboardRemove()) 
            await state.set_state(MakePost.clotype)
      
@make_post_router.message(content_types=types.ContentType.LOCATION, state = MakePost.geo2)
async def get_geo2(message: types.Message, state = FSMContext):  
    userid = message.from_user.id
    lang = await get_lang(userid)
    answer = get_action(userid)  
    cords = str(message.location.latitude) + ' ' + str(message.location.longitude)
    await state.update_data(geo=cords) 
    await bot.send_message(userid,cords)
    if answer == 'home':
        await bot.send_message(userid,make_post[lang][1],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.amountbed)
    elif answer == 'food':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'medical care':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'essentials':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'psychological help':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'kids products':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'transport':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'products for pets':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'other':
        await bot.send_message(userid,make_post[lang][8],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.helptype)
    elif answer == 'clothes':
        await bot.send_message(userid,make_post[lang][9],reply_markup=types.ReplyKeyboardRemove()) 
        await state.set_state(MakePost.clotype)

    
@make_post_router.message(state = MakePost.clotype)
async def get_clotype(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    await state.update_data(clotype=message.text)
    await state.set_state(MakePost.closize)
    await bot.send_message(userid,make_post[lang][10],reply_markup=types.ReplyKeyboardRemove())
    
make_post_router.message(state = MakePost.closize)
async def get_closize(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    await state.update_data(closize=message.text)
    await state.set_state(MakePost.comment)
    await bot.send_message(userid,make_post[lang][6],reply_markup=types.ReplyKeyboardRemove())
    
    
@make_post_router.message(state = MakePost.helptype)
async def get_helptype(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    await state.update_data(helptype=message.text)
    await state.set_state(MakePost.comment)
    await bot.send_message(userid,make_post[lang][6],reply_markup=types.ReplyKeyboardRemove())
    
    
@make_post_router.message(state = MakePost.amountbed)
async def get_amount_bed(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    try:
        await state.update_data(amountbed=int(message.text))
    except:
        await bot.send_message(userid,make_post[lang][2],reply_markup=types.ReplyKeyboardRemove())
        return
    await state.set_state(MakePost.time_for_live)
    await bot.send_message(userid,make_post[lang][3],reply_markup=types.ReplyKeyboardRemove())    
    
@make_post_router.message(state = MakePost.time_for_live)
async def get_time(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    await state.update_data(time_for_live=message.text)
    bool_answers = bool_answer(lang)
    await bot.send_message(userid,make_post[lang][4],reply_markup=bool_answers.as_markup(resize_keyboard=True))
    await state.set_state(MakePost.pets)
    
       
    
@make_post_router.message(state = MakePost.pets)
async def get_pets(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    if message.text == 'Да':
        answ = True
    else:
        answ = False
    await state.update_data(pets=answ)
    await bot.send_message(userid,make_post[lang][5],reply_markup=types.ReplyKeyboardRemove())
    print(make_post[lang][5])
    await state.set_state(MakePost.photo)
    


@make_post_router.message(content_types=['photo'], state = MakePost.photo)
async def get_photo(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    lang = await get_lang(userid)
    file = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
    file_path = file.file_path
    num = random.randint(1,1000000)
    await bot.download_file(file_path, 'tgbot/img/posts_home/'+ str(userid) + str(num) +'.jpg')
    await state.update_data(photo=str(num))
    await bot.send_message(userid,make_post[lang][6],reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(MakePost.comment)
    
    

    
@make_post_router.message(state = MakePost.comment)
async def get_comment(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    answer = get_action(userid)
    lang = await get_lang(userid)
    await state.update_data(comment = message.text)
    
    if answer == 'home':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_home(userid,type,user_data['geo'],user_data['amountbed'],user_data['time_for_live'],user_data['pets'],user_data['comment'],user_data['photo'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'food':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_home(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'medical care':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_medical_care(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'clothes':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_clothes(userid,type,user_data['geo'],user_data['clotype'],user_data['closize'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'essentials':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_first_help(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'kids products':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_kids(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'other':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_other(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'products for pets':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_pets(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'psychological help':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_psy(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()
    elif answer == 'transport':
        type = get_type(userid)
        user_data = await state.get_data()
        await posts_db.make_post_transport(userid,type,user_data['geo'],user_data['helptype'],user_data['comment'],str(message.contact.phone_number))
        await bot.send_message(userid,make_post[lang][7],reply_markup=types.ReplyKeyboardRemove()) 
        await state.clear()