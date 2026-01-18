from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot.handlers.paid_media import handle_paid_media

router = Router(name=__name__)


@router.message(Command("paid_media"))
async def process_paid_media(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Send paid media from a provided photo with a caption and price."""
    await handle_paid_media(message, bot, i18n)
