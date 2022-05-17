from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message
from tgbot.keyboards.inline.lang import lang
from tgbot.keyboards.inline.type import type_en, type_ru, type_uk
from tgbot.keyboards.inline.helpBut import help_buttons
from tgbot.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from tgbot.db import user_update
from tgbot.misc.auf_status import auf_status
from tgbot.misc.get_lang import get_lang
    
    
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

user_router = Router()


@user_router.message(commands=["start"])
async def user_start(message: Message):
    await message.reply("Привіт " + message.from_user.first_name + "!\nЦей бот створений для тих, хто потребує допомоги чи може допомогти іншим.\nОбери мову", reply_markup=lang.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'ru')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    await bot.send_message(userid, 'Выбран русский язык')
    auf_statuss = await auf_status(userid)
    if auf_statuss == False:
        await user_update.reg_user(userid,callback_query.from_user.username,'ru')
    else:
        await user_update.update_lang(userid,'ru')
    await bot.send_message(userid, 'Выбебрите пожалуйста кто вы',reply_markup=type_ru.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'en')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    await bot.send_message(userid, 'Selected English')
    auf_statuss = await auf_status(userid)
    if auf_statuss == False:
        await user_update.reg_user(userid,callback_query.from_user.username,'en')
    else:
        await user_update.update_lang(userid,'en')
    await bot.send_message(callback_query.from_user.id, 'Select please hwo are you',reply_markup=type_en.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'uk')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    await bot.send_message(userid, 'Обрана укрїнська мова')
    auf_statuss = await auf_status(userid)
    if auf_statuss == False:
        await user_update.reg_user(userid,callback_query.from_user.username,'uk')
    else:
        await user_update.update_lang(userid,'uk')
    await bot.send_message(userid, 'Оберіть хто ви',reply_markup=type_ru.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'volounter')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    lang = await get_lang(userid)
    help_but = help_buttons(lang)
    await bot.send_message(userid, 'вы стали волонтёром', reply_markup=help_but.as_markup())
    await user_update.update_status(userid,'volounter')
    
@user_router.callback_query(lambda c: c.data == 'needy')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    lang = await get_lang(userid)
    help_but = help_buttons(lang)
    await bot.send_message(userid, 'вы стали needy', reply_markup=help_but.as_markup())
    await user_update.update_status(userid,'needy')

