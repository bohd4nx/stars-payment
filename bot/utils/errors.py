from aiogram_i18n import I18nContext

ERROR_KEYS: dict[str, str] = {
    "CHARGE_ALREADY_REFUNDED": "charge-already-refunded",
    "CHARGE_NOT_FOUND": "charge-not-found",
    "REFUND_FAILED": "refund-failed",
    "DEFAULT": "refund-default"
}


def _format_tx_id(tx_id: str) -> str:
    return f"{tx_id[:6]}...{tx_id[-6:]}" if len(tx_id) > 12 else tx_id


def get_error_message(
        i18n: I18nContext,
        error_text: str,
        user_id: int | None,
        transaction_id: str | None,
) -> str:
    upper = error_text.upper() if error_text else ""
    error_code = next((code for code in ERROR_KEYS if code in upper), "DEFAULT")
    key = ERROR_KEYS.get(error_code, ERROR_KEYS["DEFAULT"])
    tx_short = _format_tx_id(transaction_id) if transaction_id else "-"
    return i18n.get(
        key,
        tx_short=tx_short,
        user_id=str(user_id),
        error=error_text
    )
