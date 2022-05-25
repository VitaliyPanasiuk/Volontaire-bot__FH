from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types


lang = InlineKeyboardBuilder()
lang.add(types.InlineKeyboardButton(
    text="English",
    callback_data="en")
)
lang.add(types.InlineKeyboardButton(
    text="Українська",
    callback_data="uk")
)
lang.add(types.InlineKeyboardButton(
    text="Русский",
    callback_data="ru")
)

# phone = ReplyKeyboardBuilder()
# phone.add(types.KeyboardButton(
#     text="send_contact",
#     request_contact=True)
# )

def send_phone(language):
    phone = ReplyKeyboardBuilder()
    if language == "en":
        phone.add(types.KeyboardButton(
        text="send contact",
        request_contact=True)
        )
    elif language == 'ru':
        phone.add(types.KeyboardButton(
        text="отправить номер",
        request_contact=True)
        )
    elif language == 'uk':
        phone.add(types.KeyboardButton(
        text="надіслати номер",
        request_contact=True)
        )
    return phone
