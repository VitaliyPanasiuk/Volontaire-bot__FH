from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types



from tgbot.misc.texts import phrases, showPost

def posts_buttons(lang):
    posts_buttons = InlineKeyboardBuilder()
    posts_buttons.row(types.InlineKeyboardButton(
        text=showPost[lang][4],
        callback_data='confirm_post')
    )
    posts_buttons.add(types.InlineKeyboardButton(
            text=showPost[lang][5],
            callback_data='reject_post')
        )
    return posts_buttons