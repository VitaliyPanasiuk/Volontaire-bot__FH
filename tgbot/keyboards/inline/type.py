from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types


type_en = InlineKeyboardBuilder()
type_en.add(types.InlineKeyboardButton(
    text="volounter",
    callback_data="volounter")
)
type_en.add(types.InlineKeyboardButton(
    text="needy",
    callback_data="needy")
)

type_ru = InlineKeyboardBuilder()
type_ru.add(types.InlineKeyboardButton(
    text="volounter",
    callback_data="volounter")
)
type_ru.add(types.InlineKeyboardButton(
    text="needy",
    callback_data="needy")
)

type_uk = InlineKeyboardBuilder()
type_uk.add(types.InlineKeyboardButton(
    text="volounter",
    callback_data="volounter")
)
type_uk.add(types.InlineKeyboardButton(
    text="needy",
    callback_data="needy")
)