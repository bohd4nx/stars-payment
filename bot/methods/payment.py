from aiogram import Router, F, html, Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from bot.utils import MESSAGES
from config import STARS_AMOUNT

router = Router(name=__name__)


@router.message(Command("start"))
async def process_pay_command(message: Message, bot: Bot) -> None:
    prices = [LabeledPrice(label='Stars Payment', amount=STARS_AMOUNT)]

    try:
        await bot.send_invoice(
            chat_id=message.chat.id,
            title='Stars Payment Example',
            description='Payment for services via Stars.',
            provider_token="",  # Empty string for payments in Telegram Stars
            currency="XTR",  # XTR for payments in Telegram Stars
            prices=prices,  # Must contain exactly one item for payments in Telegram Stars
            start_parameter='stars-payment',
            payload='stars-payment-payload'
            # Optional parameters for Stars payments:
            # business_connection_id=None,  # Unique identifier of the business connection
            # subscription_period=None,     # Number of seconds subscription will be active (must be 2592000/30 days)
            # photo_url=None,               # URL of product photo for the invoice
            # photo_size=None,              # Photo size in bytes
            # photo_width=None,             # Photo width
            # photo_height=None,            # Photo height
        )

        # Alternative: create payment link instead of direct invoice
        # invoice_link = await bot.create_invoice_link(
        #     title='Stars Payment Example',
        #     description='Payment for services via Stars.',
        #     payload='stars-payment-payload',
        #     provider_token="",
        #     currency="XTR",
        #     prices=prices
        # )
        # await message.answer(f"Payment link: {invoice_link}")
    except TelegramAPIError:
        await message.reply(MESSAGES["payment"]["error"])


@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.successful_payment)
async def process_successful_payment(message: Message) -> None:
    payment_info = message.successful_payment

    await message.reply(
        MESSAGES["payment"]["success"].format(
            amount=payment_info.total_amount,
            transaction_id=html.quote(payment_info.telegram_payment_charge_id)
        )
    )
