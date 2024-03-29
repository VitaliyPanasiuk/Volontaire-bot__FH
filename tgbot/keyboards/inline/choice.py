from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types

from tgbot.misc.get_type import get_type
from tgbot.misc.get_action import get_action

from tgbot.misc.texts import phrases, buttons_neddy


def choice_buttons_home(lang,userid):
    answer = get_type(userid)
    action = get_action(userid)
    if answer == 'volunteer':
        choice_buttons = InlineKeyboardBuilder()
        keys = [*phrases[lang]][15:19]
        k = 0
        for i in keys:
            choice_buttons.row(types.InlineKeyboardButton(
                text=phrases[lang][i],
                callback_data=keys[k])
            )
            k += 1
        choice_buttons.row(types.InlineKeyboardButton(
                text=phrases[lang]['back'],
                callback_data='helpbutton')
            )
    elif answer == 'needy':
        choice_buttons = InlineKeyboardBuilder()
        keys = [*buttons_neddy[lang]]
        k = 0
        for i in keys:
            choice_buttons.row(types.InlineKeyboardButton(
                text=buttons_neddy[lang][i],
                callback_data=keys[k])
            )
            k += 1
        choice_buttons.row(types.InlineKeyboardButton(
                    text=phrases[lang]['postig sites'],
                    callback_data='postig sites')
                )
        choice_buttons.row(types.InlineKeyboardButton(
                text=phrases[lang]['back'],
                callback_data='helpbutton')
            )
    return choice_buttons


def choice_buttons(lang,userid):
    answer = get_type(userid)
    action = get_action(userid)
    print(answer)
    choice_buttons = InlineKeyboardBuilder()
    if answer == 'volunteer':
        
        keys = [*phrases[lang]][15:18]
        k = 0
        for i in keys:
            choice_buttons.row(types.InlineKeyboardButton(
                text=phrases[lang][i],
                callback_data=keys[k])
            )
            k += 1
        choice_buttons.row(types.InlineKeyboardButton(
                text=phrases[lang]['back'],
                callback_data='helpbutton')
            )
    elif answer == 'needy':
        keys = [*buttons_neddy[lang]]
        k = 0
        print(buttons_neddy[lang])
        print(keys)
        for i in keys:
            choice_buttons.row(types.InlineKeyboardButton(
                text=buttons_neddy[lang][i],
                callback_data=keys[k])
            )
            k += 1
        if action == 'psychological help':
            choice_buttons.row(types.InlineKeyboardButton(
                    text=phrases[lang]['psysites'],
                    callback_data='psysites')
                )
        elif action == 'transport':
            choice_buttons.row(types.InlineKeyboardButton(
                    text=phrases[lang]['transportsites'],
                    callback_data='transportsites')
                )
        choice_buttons.row(types.InlineKeyboardButton(
                text=phrases[lang]['back'],
                callback_data='helpbutton')
            )
        
    return choice_buttons