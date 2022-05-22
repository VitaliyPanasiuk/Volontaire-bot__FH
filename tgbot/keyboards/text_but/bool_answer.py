from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types

from tgbot.misc.texts import regions, boll_answer

def bool_answer(language):
    bool_buttons = ReplyKeyboardBuilder()
    for i in boll_answer[language]:
        bool_buttons.add(types.KeyboardButton(text=str(i)))
    bool_buttons.adjust(2)
    return bool_buttons
