from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n import I18nContext

router = Router(name=__name__)


@router.message(Command("balance"))
async def process_balance(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Send the bot's current Stars balance."""
    balance = await bot.get_my_star_balance()
    me = await bot.me()
    await message.reply(
        i18n.get("balance-info", username=me.username, amount=balance.amount)
    )
