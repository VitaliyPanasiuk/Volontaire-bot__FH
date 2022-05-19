import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.handlers.admin import admin_router
from tgbot.handlers.get_links import get_links_router
from tgbot.handlers.user import user_router
from tgbot.handlers.make_post import make_post_router
from tgbot.handlers.help_buttons.home_but import home_router
from tgbot.handlers.help_buttons.back import back_router
from tgbot.handlers.help_buttons.clothes import clothes_router
from tgbot.handlers.help_buttons.donate import donate_router
from tgbot.handlers.help_buttons.essentials import essentials_router
from tgbot.handlers.help_buttons.food import food_router
from tgbot.handlers.help_buttons.kids_products import kids_products_router
from tgbot.handlers.help_buttons.medical_care import medical_care_router
from tgbot.handlers.help_buttons.other import other_router
from tgbot.handlers.help_buttons.produtcs_for_pets import products_for_pets_router
from tgbot.handlers.help_buttons.psychological_help import psychological_help_router
from tgbot.handlers.help_buttons.transport import transport_router
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.services import broadcaster

from tgbot.db import postgre_users_db


logger = logging.getLogger(__name__)


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Бот був запущений")


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    for router in [
        admin_router,
        user_router,
        home_router,
        get_links_router,
        back_router,
        clothes_router,
        donate_router,
        essentials_router,
        food_router,
        kids_products_router,
        medical_care_router,
        other_router,
        products_for_pets_router,
        psychological_help_router,
        transport_router,
        make_post_router,
    ]:
        dp.include_router(router)

    register_global_middlewares(dp, config)

    await on_startup(bot, config.tg_bot.admin_ids)
    await postgre_users_db.postgre_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот був вимкнений!")
