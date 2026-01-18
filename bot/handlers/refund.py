"""
Refund handler logic.

Parses user and transaction identifiers from the command payload and attempts
to refund a Stars payment with structured error reporting.
"""

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot.utils import get_error_message


def _parse_refund_args(text: str) -> tuple[int | None, str | None]:
    parts = text.split()
    if len(parts) != 3:
        return None, None
    try:
        return int(parts[1]), parts[2]
    except ValueError:
        return None, None


async def handle_refund(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Process a refund request by user and transaction id."""
    text = message.text or ""
    user_id, transaction_id = _parse_refund_args(text)
    if user_id is None or transaction_id is None:
        await message.reply(i18n.get("refund-invalid"))
        return

    try:
        result = await bot.refund_star_payment(
            user_id=user_id,
            telegram_payment_charge_id=transaction_id,
        )
        if result:
            await message.reply(i18n.get("refund-success"))
        else:
            await message.reply(i18n.get("refund-error", error="Unknown error"))
    except TelegramAPIError as exc:
        await message.reply(get_error_message(i18n, str(exc), user_id, transaction_id))
