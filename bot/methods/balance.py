from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from bot.utils import MESSAGES

router = Router(name=__name__)


@router.message(Command("balance"))
async def process_balance(message: Message, bot: Bot) -> None:
    balance = await bot.get_my_star_balance()
    me = await bot.me()
    await message.reply(
        MESSAGES["balance"]["info"].format(
            username=me.username,
            amount=balance.amount
        )
    )
