<div align="center">
   <img src="files/stars.svg" alt="Telegram Stars Payment Bot Logo" width="140" height="140" style="border-radius:24px; box-shadow:0 4px 12px rgba(0,0,0,0.25);">

   <h1 style="margin-top: 24px; font-size:42px;">Telegram Stars Payment Bot</h1>

   <p style="font-size:18px; color:#555; max-width:640px; line-height:1.4;">
      <strong>Process Telegram Stars payments, issue refunds, and monitor bot balance with localized error handling.</strong>
   </p>

   <p>
      <a href="https://github.com/bohd4nx/stars-payment/issues">Report Bug</a>
      ·
      <a href="https://github.com/bohd4nx/stars-payment/issues">Request Feature</a>
      ·
      <a href="https://t.me/bohd4nx">Contact Author</a>
   </p>
</div>

---

## Features

- Create Stars payment invoice via `/start`
- Alternative: generate payment link (commented example in `payment.py`)
- Perform refunds with `/refund <user_id> <transaction_id>`
- View bot Stars balance using `/balance`
- Clear, structured refund error messages (Telegram charge status aware)

## Screenshot / Example

<div align="center">
   <img src="files/example.png" alt="Example Stars Payment Flow" width="1150" style="border:1px solid #ddd; border-radius:12px;">
</div>

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/bohd4nx/stars-payment.git
cd stars-payment
pip install -r requirements.txt
```

### 2. Configuration

Edit `config.py`:

```python
API_TOKEN = "your_bot_token_here"  # Obtain at @BotFather
```

### 3. Run

```bash
python main.py
```

## Commands

| Command                              | Description                             |
| ------------------------------------ | --------------------------------------- |
| `/start`                             | Send a Stars payment invoice            |
| `/refund <user_id> <transaction_id>` | Attempt refund of a prior Stars payment |
| `/balance`                           | Show current Stars balance of the bot   |

---

<div align="center" style="margin-top:32px;">
   <p><strong>Made with ❤️ by <a href="https://t.me/bohd4nx" target="_blank">@bohd4nx</a></strong></p>
   <p>Star ⭐ this repo if it helps your Telegram payments!</p>
</div>
