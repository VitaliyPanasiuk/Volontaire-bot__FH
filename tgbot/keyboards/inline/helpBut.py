from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types
# from dotenv import get_key
from tgbot.misc.texts import phrases

# def get_key(d, value):
#     for k, v in d.items():
#         if v == value:
#             return k

def help_buttons(lang):
    help_buttons = InlineKeyboardBuilder()
    keys = [*phrases[lang]][2:13]
    print(keys)
    k = 0
    for i in keys:
        print(i)
        help_buttons.row(types.InlineKeyboardButton(
            text=phrases[lang][i],
            callback_data=keys[k])
        )
        k += 1
    return help_buttons