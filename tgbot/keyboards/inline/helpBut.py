from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from aiogram import Bot, types



from tgbot.misc.texts import phrases


def help_buttons(lang):
    help_buttons = InlineKeyboardBuilder()
    keys = [*phrases[lang]][2:13]
    k = 0
    for i in keys:
        help_buttons.row(types.InlineKeyboardButton(
            text=phrases[lang][i],
            callback_data=keys[k])
        )
        k += 1
    help_buttons.add(types.InlineKeyboardButton(
            text=phrases[lang]['back'],
            callback_data='homeback')
        )
    return help_buttons

def donate_buttons(lang):
    donate_buttons = InlineKeyboardBuilder()
    donate_buttons.row(types.InlineKeyboardButton(
            text=phrases[lang]['liqpay'],
            url = 'https://www.liqpay.ua/checkout/sandbox_i46393644366',
            callback_data='donate_liq')
        )
    donate_buttons.row(types.InlineKeyboardButton(
            text=phrases[lang]['army'],
            url = 'https://bank.gov.ua/ua/news/all/natsionalniy-bank-vidkriv-spetsrahunok-dlya-zboru-koshtiv-na-potrebi-armiyi',
            callback_data='donate_army')
        )
    donate_buttons.row(types.InlineKeyboardButton(
            text=phrases[lang]['runner'],
            url = 'https://savelife.in.ua/',
            callback_data='donate_runner')
        )
    donate_buttons.row(types.InlineKeyboardButton(
            text=phrases[lang]['back'],
            callback_data='helpbutton')
        )
    return donate_buttons