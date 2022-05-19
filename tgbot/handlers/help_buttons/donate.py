from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message
from tgbot.keyboards.inline.lang import lang
from tgbot.keyboards.inline.type import type_en, type_ru, type_uk
from tgbot.keyboards.inline.helpBut import help_buttons
from tgbot.keyboards.inline.choice import choice_buttons
from tgbot.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from tgbot.db import user_update
from tgbot.misc.auf_status import auf_status
from tgbot.misc.get_lang import get_lang

from tgbot.misc.texts import phrases
    
    
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

donate_router = Router()


@donate_router.callback_query(lambda c: c.data == 'donate')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    lang = await get_lang(userid)
    choice_but = choice_buttons(lang,userid)
    await bot.send_message(userid, phrases[lang]['after_type'], reply_markup=choice_but.as_markup())