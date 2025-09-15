ERROR_HANDLERS = {
    "CHARGE_ALREADY_REFUNDED": {
        "message": "💰 <b>Refund already processed</b>\n\n"
                   "🆔 <b>Transaction:</b> <code>{tx_short}</code>\n"
                   "👤 <b>User ID:</b> <code>{user_id}</code>\n\n"
                   "ℹ️ This payment has already been refunded."
    },
    "CHARGE_NOT_FOUND": {
        "message": "❓ <b>Transaction not found</b>\n\n"
                   "🆔 <b>Transaction:</b> <code>{tx_short}</code>\n"
                   "👤 <b>User ID:</b> <code>{user_id}</code>\n\n"
                   "⚠️ The specified transaction does not exist."
    },
    "REFUND_FAILED": {
        "message": "❌ <b>Refund failed</b>\n\n"
                   "🆔 <b>Transaction:</b> <code>{tx_short}</code>\n"
                   "👤 <b>User ID:</b> <code>{user_id}</code>\n\n"
                   "⚠️ The bot may have insufficient balance or a Telegram-side error occurred."
    },
    "DEFAULT": {
        "message": "❌ <b>Refund failed</b>\n\n"
                   "🆔 <b>Transaction:</b> <code>{tx_short}</code>\n"
                   "👤 <b>User ID:</b> <code>{user_id}</code>\n\n"
                   "💭 <b>Error details:</b>\n<pre>{error}</pre>"
    }
}


def _format_tx_id(tx_id: str) -> str:
    return f"{tx_id[:6]}...{tx_id[-6:]}" if len(tx_id) > 12 else tx_id


def get_error_message(error_text: str, user_id: int, transaction_id: str) -> str:
    error_code = next((code for code in ERROR_HANDLERS if code in error_text.upper()), "DEFAULT")
    tx_short = _format_tx_id(transaction_id)

    return ERROR_HANDLERS[error_code]["message"].format(
        tx_short=tx_short,
        user_id=user_id,
        error=error_text
    )
