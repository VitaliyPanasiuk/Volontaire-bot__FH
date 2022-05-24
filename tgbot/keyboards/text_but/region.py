from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types

from tgbot.misc.texts import regions

def choice_region(lang):
    region_buttons = ReplyKeyboardBuilder()
    for i in regions[lang]:
        region_buttons.add(types.KeyboardButton(text=str(i)))
    if lang == 'ru':
        region_buttons.row(
            types.KeyboardButton(text="Запросить геолокацию")
        )
    elif lang == 'en':
        region_buttons.row(
            types.KeyboardButton(text="Request geolocation")
        )
    elif lang == 'uk':
        region_buttons.row(
            types.KeyboardButton(text="Запросити геолокацію")
        )
    region_buttons.adjust(2)
    return region_buttons
