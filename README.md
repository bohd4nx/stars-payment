<div align="center">
   <h1>⭐️ Telegram Stars Payment Bot</h1>
   <p>Complete Telegram bot for Stars payments and refunds using aiogram 3.x</p>
</div>

## Features

- **Payment processing** via Telegram Stars with invoice generation
- **Refund functionality** with detailed error handling and validation
- **Balance cheking** for bot's Stars balance
- **Error management** with user-friendly messages
- **Clean architecture** with modular design

## Commands

| Command                              | Description                            |
|--------------------------------------|----------------------------------------|
| `/start`                             | Create and send Stars payment invoice  |
| `/refund <user_id> <transaction_id>` | Process payment refund with validation |
| `/balance`                           | Display bot's current Stars balance    |

## Setup

1. **Clone and install:**
   ```bash
   git clone https://github.com/bohd4nx/tg-stars-payment.git
   cd tg-stars-payment
   pip install -r requirements.txt
   ```

2. **Configure bot:**
   ```python
   # config.py
   API_TOKEN = "your_bot_token_here"  # From @BotFather
   STARS_AMOUNT = 1                   # Payment amount (1-100000 stars)
   ```

3. **Run bot:**
   ```bash
   python main.py
   ```

## Error Handling

The bot includes comprehensive error handling for common scenarios:

- **CHARGE_ALREADY_REFUNDED** - Payment already refunded
- **CHARGE_NOT_FOUND** - Transaction not found
- **REFUND_FAILED** - Insufficient bot balance or Telegram error
- **Invalid commands** - Proper format guidance

---

<div align="center">
    <h4>Built with ❤️ by <a href="https://t.me/bohd4nx" target="_blank">Bohdan</a></h4>
</div>
