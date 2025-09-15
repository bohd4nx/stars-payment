import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from bot.methods import payment_router, refund_router, balance_router
from config import API_TOKEN

logging.basicConfig(
    level=logging.ERROR,
    format='[%(asctime)s] - %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
dispatcher_logger = logging.getLogger('aiogram.dispatcher')
dispatcher_logger.setLevel(logging.INFO)

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

routers = {
    "payment": payment_router,
    "refund": refund_router,
    "balance": balance_router,
}

for router in routers.values():
    dp.include_router(router)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
