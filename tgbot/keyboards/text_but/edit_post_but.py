from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types

from tgbot.misc.texts import regions

def choice_edit_action():
    region_buttons = ReplyKeyboardBuilder()
    region_buttons.add(
        types.KeyboardButton(text="Edit")
    )
    region_buttons.add(
        types.KeyboardButton(text="Delete")
    )
    region_buttons.adjust(2)
    return region_buttons