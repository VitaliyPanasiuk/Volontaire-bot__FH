from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message
from tgbot.keyboards.inline.lang import lang
from tgbot.keyboards.inline.type import type_en, type_ru, type_uk
from tgbot.keyboards.inline.helpBut import help_buttons, donate_buttons
from tgbot.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from tgbot.db import user_update
from tgbot.misc.auf_status import auf_status
from tgbot.misc.get_lang import get_lang
from tgbot.misc.texts import phrases
from tgbot.misc.get_action import get_action

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

get_links_router = Router()


@get_links_router.callback_query(lambda c: c.data == 'psysites')
async def psysites(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    await bot.send_message(userid, 'https://t.me/friend_first_aid_bot?fbclid=IwAR1Q-s9Was_brDIJbZBGep-yWWdJNtVhQYbS6mgE5YlJs4cPm4QollWrvvM', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(userid, 'https://calendly.com/resiliencehub/30-min-consultations?month=2022-05', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(userid, 'https://tellme.com.ua/', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(userid, 'https://docs.google.com/forms/d/e/1FAIpQLSe-x6XZmhEG6X3smpo3eniRlX1JOwo7CLKJ9aunQ_1L_H1weg/viewform', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(userid, 'https://t.me/psysupportua_bot', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(userid, 'https://poruch.me/?fbclid=IwAR08FrW_Pdi-Nq5vaEdl7Z04RpxtIOqxyqIVBM3bhTgmxrwZjGddv_3auTo', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(userid, 'https://ukr-ednist.com.ua/', reply_markup=types.ReplyKeyboardRemove())
    
@get_links_router.callback_query(lambda c: c.data == 'transportsites')
async def psysites(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id   
    await bot.send_message(userid, 'https://www.blablacar.com.ua/', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://bolt.eu/', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://uz.gov.ua/', reply_markup=types.ReplyKeyboardRemove()) 
    
@get_links_router.callback_query(lambda c: c.data == 'postig sites')
async def psysites(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id   
    await bot.send_message(userid, 'https://everybedhelps.com/', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://wunderflats.com/page/ukraine/tenants-in-need-ua', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://ua.eu4ua.org/refugees', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://icanhelp.host/', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://homesforukraine.eu/en/home-eng/', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://prykhystok.in.ua/find', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://www.living-hotels.com/help/', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://mapahelp.me/', reply_markup=types.ReplyKeyboardRemove()) 
    await bot.send_message(userid, 'https://www.shelter4ua.com/home/i-need-help', reply_markup=types.ReplyKeyboardRemove()) 
    
    

@get_links_router.callback_query(lambda c: c.data == 'donate')
async def psysites(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id 
    language = await get_lang(userid)
    donate_button = donate_buttons(language)
    await bot.send_message(userid, phrases[language]['liq'], reply_markup=donate_button.as_markup()) 
    
