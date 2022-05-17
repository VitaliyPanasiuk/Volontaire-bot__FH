from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types


lang = InlineKeyboardBuilder()
lang.add(types.InlineKeyboardButton(
    text=" англійська",
    callback_data="en")
)
lang.add(types.InlineKeyboardButton(
    text="українська",
    callback_data="uk")
)
lang.add(types.InlineKeyboardButton(
    text="русский",
    callback_data="ru")
)