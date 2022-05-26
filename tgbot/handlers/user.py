from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message
from tgbot.keyboards.inline.lang import lang, send_phone
from tgbot.keyboards.inline.type import type_en, type_ru, type_uk
from tgbot.keyboards.inline.helpBut import help_buttons
from tgbot.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardButton,InlineKeyboardBuilder
from tgbot.db import user_update
from tgbot.misc.auf_status import auf_status
from tgbot.misc.get_lang import get_lang
from tgbot.misc.get_type import get_type
from tgbot.misc.states import getNumber
from tgbot.misc.texts import phrases
from tgbot.misc.get_action import get_action
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
    
    
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

user_router = Router()


@user_router.message(commands=["start"])
async def user_start(message: Message):
    await message.reply("Привіт " + message.from_user.first_name + "!\nЦей бот створений для тих, хто потребує допомоги чи може допомогти іншим.\nОбери мову", reply_markup=lang.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'ru')
async def user_start(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    await bot.send_message(userid, 'Выбран русский язык')
    auf_statuss = await auf_status(userid)
    phone = send_phone('ru')
    if auf_statuss == False:
        await bot.send_message(userid, 'Отправьте свой номер телефона или впишите его самостоятельно', reply_markup=phone.as_markup(resize_keyboard=True))
        await state.set_state(getNumber.num)
    else:
        await user_update.update_lang(userid,'ru')
        await bot.send_message(userid, 'Выберите пожалуйста кто вы',reply_markup=type_ru.as_markup())
    

@user_router.callback_query(lambda c: c.data == 'en')
async def user_start(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    await bot.send_message(userid, 'Selected English')
    auf_statuss = await auf_status(userid)
    phone = send_phone('en')
    if auf_statuss == False:
        await bot.send_message(userid, 'Send your phone number or enter it yourself', reply_markup=phone.as_markup(resize_keyboard=True))
        await state.set_state(getNumber.num2)     
    else:
        await user_update.update_lang(userid,'en')
        await bot.send_message(callback_query.from_user.id, 'Please choose who you are',reply_markup=type_en.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'uk')
async def user_start(callback_query: types.CallbackQuery, state = FSMContext):
    userid = callback_query.from_user.id
    await bot.send_message(userid, 'Обрана укрїнська мова')
    auf_statuss = await auf_status(userid)
    phone = send_phone('uk')
    if auf_statuss == False:
        await bot.send_message(userid, 'Надішліть свій номер телефону або впишіть його самостійно', reply_markup=phone.as_markup(resize_keyboard=True))
        await state.set_state(getNumber.num3)  
    else:
        await user_update.update_lang(userid,'uk')
        await bot.send_message(userid, 'Виберіть будь ласка, хто ви',reply_markup=type_uk.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'volunteer')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    language = await get_lang(userid)
    help_but = help_buttons(language)
    await bot.send_message(userid, phrases[language]['volunteer'], reply_markup=help_but.as_markup())
    await user_update.update_status(userid,'volunteer')
    
@user_router.callback_query(lambda c: c.data == 'needy')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    language = await get_lang(userid)
    print(language)
    help_but = help_buttons(language)
    await bot.send_message(userid, phrases[language]['needy'], reply_markup=help_but.as_markup())
    await user_update.update_status(userid,'needy')

@user_router.callback_query(lambda c: c.data == 'homeback')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    language = await get_lang(userid)
    help_but = help_buttons(language)
    await bot.send_message(userid,"Привіт " + callback_query.from_user.first_name + "!\nЦей бот створений для тих, хто потребує допомоги чи може допомогти іншим.\nОбери мову", reply_markup=lang.as_markup())
    
@user_router.callback_query(lambda c: c.data == 'helpbutton')
async def user_start(callback_query: types.CallbackQuery):
    userid = callback_query.from_user.id
    language = await get_lang(userid)
    help_but = help_buttons(language)
    answer = get_type(userid)
    print(answer)
    if answer == 'volunteer':
        await bot.send_message(userid, phrases[language]['volunteer'], reply_markup=help_but.as_markup())
    else:
        await bot.send_message(userid, phrases[language]['needy'], reply_markup=help_but.as_markup())


@user_router.message_handler(content_types=types.ContentType.ANY, state=getNumber.num)
async def contacts(msg: types.Message, state: FSMContext):
    userid = msg.from_user.id
    if msg.content_type =='contact':
        await user_update.reg_user(userid,userid,'ru',str(msg.contact.phone_number))
        await state.clear() 
    elif msg.content_type == 'text':
        await user_update.reg_user(userid,userid,'ru',str(msg.text))
        await state.clear() 
    
    await bot.send_message(userid, 'Выберите пожалуйста кто вы',reply_markup=type_ru.as_markup())
    
@user_router.message_handler(content_types=types.ContentType.CONTACT, state=getNumber.num2)
async def contacts(msg: types.Message, state: FSMContext):
    userid = msg.from_user.id
    if msg.content_type =='contact':
        await user_update.reg_user(userid,userid,'en',str(msg.contact.phone_number))
        await state.clear() 
    elif msg.content_type == 'text':
        await user_update.reg_user(userid,userid,'en',str(msg.text))
        await state.clear() 
    await bot.send_message(userid, 'Please choose who you are',reply_markup=type_ru.as_markup())
    
@user_router.message_handler(content_types=types.ContentType.CONTACT, state=getNumber.num3)
async def contacts(msg: types.Message, state: FSMContext):
    userid = msg.from_user.id
    if msg.content_type =='contact':
        await user_update.reg_user(userid,userid,'en',str(msg.contact.phone_number))
        await state.clear() 
    elif msg.content_type == 'text':
        await user_update.reg_user(userid,userid,'en',str(msg.text))
        await state.clear() 
    await bot.send_message(userid, 'Виберіть будь ласка, хто ви',reply_markup=type_ru.as_markup())
