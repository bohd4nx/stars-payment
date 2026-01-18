from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot.handlers import handle_refund_transactions

router = Router(name=__name__)


@router.message(Command("refund_user"))
async def process_refund_transactions(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Refund all refundable Star transactions for a user."""
    await handle_refund_transactions(message, bot, i18n)
