from aiogram import Router, Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command
from aiogram.methods.refund_star_payment import RefundStarPayment
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot.utils import get_error_message

router = Router(name=__name__)


@router.message(Command("refund"))
async def process_refund(message: Message, bot: Bot, i18n: I18nContext) -> None:
    parts = message.text.split()
    user_id = None
    transaction_id = None

    if len(parts) != 3:
        await message.reply(i18n.get("refund-invalid"))
        return

    try:
        user_id, transaction_id = int(parts[1]), parts[2]
        result = await bot(RefundStarPayment(
            user_id=user_id,
            telegram_payment_charge_id=transaction_id
        ))

        if result:
            await message.reply(i18n.get("refund-success"))
        else:
            await message.reply(i18n.get("refund-error", error="Unknown error"))

    except ValueError:
        await message.reply(i18n.get("refund-invalid"))
    except TelegramAPIError as e:
        await message.reply(get_error_message(i18n, str(e), user_id, transaction_id))
