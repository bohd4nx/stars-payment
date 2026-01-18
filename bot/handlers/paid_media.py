"""
Paid media handler logic.

Accepts a photo and amount, then sends paid media with a Stars price and a
localized caption, returning input guidance on validation errors.
"""

from aiogram import Bot
from aiogram.types import InputPaidMediaPhoto, Message, ReplyParameters
from aiogram_i18n import I18nContext


def _extract_photo_file_id(message: Message) -> str | None:
    """Get the photo file_id from a message or replied photo."""
    if message.photo:
        return message.photo[-1].file_id
    if message.reply_to_message and message.reply_to_message.photo:
        return message.reply_to_message.photo[-1].file_id
    return None


async def handle_paid_media(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Send paid media from a provided photo with a caption and price."""
    photo_file_id = _extract_photo_file_id(message)
    text = message.text or message.caption or ""
    parts = text.split()
    if not photo_file_id or len(parts) != 2:
        await message.reply(i18n.get("paid-media-invalid"))
        return

    try:
        star_count = int(parts[1])
    except ValueError:
        await message.reply(i18n.get("paid-media-invalid"))
        return
    if not (1 <= star_count <= 25000):
        await message.reply(i18n.get("paid-media-invalid"))
        return

    caption = i18n.get("paid-media-caption")
    await bot.send_paid_media(
        chat_id=message.chat.id,
        star_count=star_count,
        media=[
            InputPaidMediaPhoto(
                media=photo_file_id,
                caption=caption,
            )
        ],
        reply_parameters=ReplyParameters(message_id=message.message_id),
    )
