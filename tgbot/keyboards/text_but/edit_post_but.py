from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types

from tgbot.misc.texts import regions

def choice_edit_action(language):
    region_buttons = ReplyKeyboardBuilder()
    if language == 'en':
        region_buttons.add(
            types.KeyboardButton(text="Edit")
        )
        region_buttons.add(
            types.KeyboardButton(text="Delete")
        )
    elif language == 'ru':
        region_buttons.add(
            types.KeyboardButton(text="Редактировать")
        )
        region_buttons.add(
            types.KeyboardButton(text="Удалить")
        )
    elif language == 'uk':
        region_buttons.add(
            types.KeyboardButton(text="Редагувати")
        )
        region_buttons.add(
            types.KeyboardButton(text="Видалити")
        )
    region_buttons.adjust(2)
    return region_buttons