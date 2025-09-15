from aiogram import Router, Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command
from aiogram.methods.refund_star_payment import RefundStarPayment
from aiogram.types import Message

from bot.utils import MESSAGES, get_error_message

router = Router(name=__name__)


@router.message(Command("refund"))
async def process_refund(message: Message, bot: Bot) -> None:
    parts = message.text.split()
    user_id = None
    transaction_id = None

    if len(parts) != 3:
        await message.reply(MESSAGES["command"]["invalid"])
        return

    handlers = {
        "success": lambda _: MESSAGES["refund"]["success"],
        "failure": lambda _: get_error_message("Unknown error", user_id, transaction_id)
    }

    try:
        user_id, transaction_id = int(parts[1]), parts[2]
        result = await bot(RefundStarPayment(
            user_id=user_id,
            telegram_payment_charge_id=transaction_id
        ))

        response_key = "success" if result else "failure"
        await message.reply(handlers[response_key](result))

    except ValueError:
        await message.reply(MESSAGES["command"]["invalid"])
    except TelegramAPIError as e:
        await message.reply(get_error_message(str(e), user_id, transaction_id))
