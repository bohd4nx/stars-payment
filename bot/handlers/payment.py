from aiogram import Router, F, html, Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram_i18n import I18nContext

router = Router(name=__name__)


@router.message(F.text.regexp(r"^\d{1,6}$"))
async def handle_amount(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """
    Flow:
      1. User sends a number 1–100000 (raw Stars units)
      2. Validate range; build single LabeledPrice (Stars requires exactly one component)
      3. Call send_invoice with currency 'XTR' and empty provider_token (rule for Stars)
      4. Optionally (commented) build a payment link instead of direct invoice.

    Core send_invoice parameters (Stars context):
      chat_id: user chat id (invoice destination)
      title: localized product/invoice title (1–32 chars)
      description: localized description (1–255 chars)
      payload: internal tracking string (NOT shown to user) – embeds amount
      currency: must be 'XTR' for Telegram Stars
      prices: list[LabeledPrice] – MUST contain exactly ONE item for Stars
      provider_token: empty string for Stars; normal fiat providers supply real token
      start_parameter: deep-link tag; forwarded copies behavior differs if present

    Optional (reference only): business_connection_id, subscription_period, photo_* metadata.
    Ignored for Stars: tips, user data requirements, shipping, flexible pricing.

    Docs: sendInvoice API – https://core.telegram.org/bots/api#sendinvoice
          Stars Overview – https://telegram.org/blog/telegram-stars
          Stars Bot API – https://core.telegram.org/bots/payments-stars
    """
    try:
        amount = int(message.text)
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
            # subscription_period=None,  # Must be 2592000 (30 days) if used
            # photo_url=None,
            # photo_size=None,
            # photo_width=None,
            # photo_height=None,
        )

        # Alternative: create a payment link instead of direct invoice.
        # Uncomment block below to send a link instead.
        # try:
        #     invoice_link = await bot.create_invoice_link(
        #         title=i18n.get("invoice-title"),
        #         description=i18n.get("invoice-description"),
        #         payload=f'stars-payment-{amount}',
        #         provider_token="",  # Empty for Stars
        #         currency="XTR",
        #         prices=[LabeledPrice(label=i18n.get("invoice-label"), amount=amount)]
        #     )
        #     await message.answer(
        #         i18n.get("payment-link", link=html.quote(invoice_link))
        #     )
        # except TelegramAPIError:
        #     pass
    except TelegramAPIError:
        await message.reply(i18n.get("invoice-error"))


@router.pre_checkout_query()
async def handle_pre_checkout(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.successful_payment)
async def handle_successful_payment(message: Message, i18n: I18nContext) -> None:
    info = message.successful_payment
    await message.reply(
        i18n.get(
            "payment-success",
            amount=info.total_amount,
            transaction_id=html.quote(info.telegram_payment_charge_id)
        )
    )
