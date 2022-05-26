from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types


type_en = InlineKeyboardBuilder()
type_en.add(types.InlineKeyboardButton(
    text="volunteer",
    callback_data="volunteer")
)
type_en.add(types.InlineKeyboardButton(
    text="needy",
    callback_data="needy")
)

type_ru = InlineKeyboardBuilder()
type_ru.add(types.InlineKeyboardButton(
    text="волонтёр",
    callback_data="volunteer")
)
type_ru.add(types.InlineKeyboardButton(
    text="нуждающийся",
    callback_data="needy")
)

type_uk = InlineKeyboardBuilder()
type_uk.add(types.InlineKeyboardButton(
    text="волонтер",
    callback_data="volunteer")
)
type_uk.add(types.InlineKeyboardButton(
    text="потребуючий",
    callback_data="needy")
)