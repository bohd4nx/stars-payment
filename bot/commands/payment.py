from aiogram import Bot, F, Router, html
from aiogram.filters import Command
from aiogram.types import Message, PreCheckoutQuery
from aiogram_i18n import I18nContext

from bot.handlers.payment import handle_pay

router = Router(name=__name__)


@router.message(Command("pay"))
async def process_pay(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Send a Stars invoice for the specified amount."""
    await handle_pay(message, bot, i18n)


@router.pre_checkout_query()
async def handle_pre_checkout(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    """Approve Stars pre-checkout queries."""
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.successful_payment)
async def handle_successful_payment(message: Message, i18n: I18nContext) -> None:
    """Notify user about a successful Stars payment."""
    info = message.successful_payment
    await message.reply(
        i18n.get(
            "payment-success",
            amount=info.total_amount,
            transaction_id=html.quote(info.telegram_payment_charge_id),
        )
    )
