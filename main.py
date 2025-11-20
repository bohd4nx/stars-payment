import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore

from bot.commands import start_router
from bot.commands.balance import router as balance_router
from bot.commands.refund import router as refund_router
from bot.handlers.payment import router as payment_handlers_router
from config import API_TOKEN

logging.basicConfig(
    level=logging.ERROR,
    format='[%(asctime)s] - %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
dispatcher_logger = logging.getLogger('aiogram.dispatcher')
dispatcher_logger.setLevel(logging.INFO)

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        link_preview_is_disabled=True
    )
)
dp = Dispatcher()

i18n_middleware = I18nMiddleware(
    core=FluentRuntimeCore(path="locales/{locale}"),
    default_locale="en"
)

dp.include_router(start_router)
dp.include_router(payment_handlers_router)
dp.include_router(balance_router)
dp.include_router(refund_router)

dp.update.middleware(i18n_middleware)
dp.message.middleware(i18n_middleware)
dp.callback_query.middleware(i18n_middleware)

i18n_middleware.setup(dispatcher=dp)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
