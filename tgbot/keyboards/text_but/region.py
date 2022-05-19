from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types

from tgbot.misc.texts import regions

def choice_region(lang):
    region_buttons = ReplyKeyboardBuilder()
    for i in regions[lang]:
        region_buttons.add(types.KeyboardButton(text=str(i)))
    region_buttons.row(
        types.KeyboardButton(text="Запросить геолокацию")
    )
    region_buttons.adjust(2)
    return region_buttons
