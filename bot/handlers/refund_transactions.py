"""
Batch refund handler logic.

Load Stars transactions, filters by user, and attempts to refund eligible
charges while tracking summary statistics.
"""

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message
from aiogram_i18n import I18nContext


def _parse_user_id(text: str) -> int | None:
    parts = text.split()
    if len(parts) != 2:
        return None
    try:
        return int(parts[1])
    except ValueError:
        return None


def _tx_user_id(tx: object) -> int | None:
    user = getattr(tx, "user", None)
    user_id = getattr(user, "id", None)
    if isinstance(user_id, int):
        return user_id
    source = getattr(tx, "source", None)
    source_user = getattr(source, "user", None)
    source_user_id = getattr(source_user, "id", None)
    if isinstance(source_user_id, int):
        return source_user_id
    return None


def _tx_charge_id(tx: object) -> str | None:
    for attr in ("telegram_payment_charge_id", "transaction_id", "id"):
        value = getattr(tx, attr, None)
        if isinstance(value, str) and value:
            return value
    source = getattr(tx, "source", None)
    for attr in ("telegram_payment_charge_id", "transaction_id", "id"):
        value = getattr(source, attr, None)
        if isinstance(value, str) and value:
            return value
    return None


async def _refund_charge(bot: Bot, user_id: int, charge_id: str) -> bool:
    try:
        return await bot.refund_star_payment(
            user_id=user_id,
            telegram_payment_charge_id=charge_id,
        )
    except TelegramAPIError:
        return False


async def handle_refund_transactions(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Refund all refundable Star transactions for a user."""
    text = message.text or message.caption or ""
    user_id = _parse_user_id(text)
    if user_id is None:
        await message.reply(i18n.get("refund-transactions-invalid"))
        return

    stats = {"scanned": 0, "refunded": 0, "skipped": 0}
    offset = 0
    limit = 100

    try:
        while True:
            result = await bot.get_star_transactions(offset=offset, limit=limit)
            transactions = result.transactions
            if not transactions:
                break

            for tx in transactions:
                stats["scanned"] += 1
                if _tx_user_id(tx) != user_id:
                    stats["skipped"] += 1
                    continue

                charge_id = _tx_charge_id(tx)
                if not charge_id:
                    stats["skipped"] += 1
                    continue

                if await _refund_charge(bot, user_id, charge_id):
                    stats["refunded"] += 1
                else:
                    stats["skipped"] += 1

            if len(transactions) < limit:
                break
            offset += len(transactions)
    except TelegramAPIError as exc:
        await message.reply(i18n.get("refund-transactions-error", error=str(exc)))
        return

    await message.reply(
        i18n.get(
            "refund-transactions-summary",
            user_id=str(user_id),
            scanned=stats["scanned"],
            refunded=stats["refunded"],
            skipped=stats["skipped"],
        )
    )
