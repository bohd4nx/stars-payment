"""
Payment handler logic.

Parses a payment amount from the /pay command and issues a Stars invoice with
validated limits and localized error responses.
"""

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message, LabeledPrice
from aiogram_i18n import I18nContext


async def handle_pay(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Validate /pay amount and send a Stars invoice (single LabeledPrice, XTR). """
    text = message.text or ""
    parts = text.split()
    if len(parts) != 2:
        await message.reply(i18n.get("amount-invalid"))
        return
    try:
        amount = int(parts[1])
    except ValueError:
        await message.reply(i18n.get("amount-invalid"))
        return
    if not (1 <= amount <= 100000):
        await message.reply(i18n.get("amount-invalid"))
        return

    try:
        await bot.send_invoice(
            chat_id=message.chat.id,
            title=i18n.get("invoice-title"),
            description=i18n.get("invoice-description"),
            provider_token="",  # Empty for Stars
            currency="XTR",  # Stars currency code
            prices=[LabeledPrice(label=i18n.get("invoice-label"), amount=amount)],  # Exactly one item
            start_parameter='stars-payment',
            payload=f'stars-payment-{amount}'  # Internal tracking
            # Optional parameters for Stars payments:
            # business_connection_id=None,
            # subscription_period=None, # Must be 2592000 (30 days) if used
            # photo_url=None,
            # photo_size=None,
            # photo_width=None,
            # photo_height=None,
        )

        # Alternative: create a payment link instead of a direct invoice.
        # Uncomment the block below to send a link instead.
        # try:
        #     invoice_link = await bot.create_invoice_link(
        #         title=i18n.get("invoice-title"),
        #         description=i18n.get("invoice-description"),
        #         payload=f'stars-payment-{amount}',
        #         provider_token="", # Empty for Stars
        #         currency="XTR",
        #         prices=[LabeledPrice(label=i18n.get("invoice-label"), amount=amount)]
        #     )
        #     await message.answer(
        #         i18n.get("payment-link", link=html.quote(invoice_link))
        #     )
        # except TelegramAPIError:
        #     pass
    except TelegramAPIError as exc:
        await message.reply(i18n.get("invoice-error", error=str(exc)))
