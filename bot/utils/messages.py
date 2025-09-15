MESSAGES = {
    "payment": {
        "success": "🎉 <b>Payment successful!</b>\n\n💵 <b>Amount:</b> {amount}⭐️\n\n🆔 <b>Transaction ID:</b> <code>{transaction_id}</code>",
        "error": "❌ <b>Failed to create payment invoice</b>"
    },
    "refund": {
        "success": "✅ <b>Payment has been successfully refunded!</b>",
        "error": "❌ <b>Failed to refund payment</b>: <pre>{error}</pre>"
    },
    "command": {
        "invalid": "❌ <b>Please use format:</b> /refund '&lt;user_id&gt;' '&lt;transaction_id&gt;'\n\nℹ️ Example: <code>/refund 123456789 ABC123XYZ</code>"
    },
    "balance": {
        "info": "💰 <b>Bot balance (@{username}):</b> {amount}⭐️"
    }
}
