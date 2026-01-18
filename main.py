import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore

from bot.commands import (
    balance_router,
    paid_media_router,
    payment_router,
    refund_router,
    refund_transactions_router,
    start_router,
)
from bot.core import config, logger, setup_logging


async def set_bot_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Start"),
        BotCommand(command="pay", description="Pay with Stars"),
        BotCommand(command="refund", description="Refund a payment"),
        BotCommand(command="refund_user", description="Refund user transactions"),
        BotCommand(command="balance", description="Show balance"),
        BotCommand(command="paid_media", description="Send paid media"),
    ]
    await bot.set_my_commands(commands)


async def setup_i18n() -> I18nMiddleware:
    i18n_core = FluentRuntimeCore(path="locales/{locale}")
    await i18n_core.startup()
    logger.info(f"Loaded locales: {i18n_core.available_locales}")
    return I18nMiddleware(core=i18n_core, default_locale="en")


def setup_middlewares(dp: Dispatcher, i18n: I18nMiddleware) -> None:
    dp.update.middleware(i18n)
    dp.message.middleware(i18n)
    dp.callback_query.middleware(i18n)
    i18n.setup(dispatcher=dp)


async def main() -> None:
    setup_logging()

    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True,
        ),
    )

    await set_bot_commands(bot)

    i18n = await setup_i18n()

    dp = Dispatcher()
    for router in [
        start_router,
        payment_router,
        balance_router,
        refund_router,
        refund_transactions_router,
        paid_media_router,
    ]:
        dp.include_router(router)

    setup_middlewares(dp, i18n)

    try:
        await dp.start_polling(
            bot,
            polling_timeout=30,
            handle_as_tasks=True,
            tasks_concurrency_limit=100,
            close_bot_session=True,
        )
    finally:
        await i18n.core.shutdown()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
    except Exception as exc:
        logger.exception(f"Unexpected error: {exc}")
