start-intro = 
    ⭐️ <b>Telegram Stars Payment Demo Bot</b>
    
    This bot demonstrates <b>payment</b>, <b>refund</b>, and <b>balance</b> features with Telegram Stars.
    
    <b>How to pay:</b> send a number (1 – 100000) as a message and you will receive an invoice for that many ⭐️.
    
    <b>Refund:</b> Use <code>/refund &lt;user_id&gt; &lt;transaction_id&gt;</code> after a successful payment.
    <b>Balance:</b> Use <code>/balance</code> to view current Stars balance of the bot.
    
    Send an amount now to generate an invoice.

refund-invalid = 
    ❌ <b>Please use format:</b> /refund '&lt;user_id&gt;' '&lt;transaction_id&gt;'
    
    ℹ️ Example: <code>/refund 123456789 ABC123XYZ</code>

refund-default = 
    ❌ <b>Refund failed</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    💭 <b>Error details:</b>
    <pre>{ $error }</pre>

refund-failed = 
    ❌ <b>Refund failed</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ⚠️ The bot may have insufficient balance or a Telegram-side error occurred.

charge-already-refunded = 
    💰 <b>Refund already processed</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ℹ️ This payment has already been refunded.

charge-not-found = 
    ❓ <b>Transaction not found</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ⚠️ The specified transaction does not exist.

payment-success = 
    🎉 <b>Payment successful!</b>
    
    💵 <b>Amount:</b> { $amount }⭐️
    
    🆔 <b>Transaction ID:</b> <code>{ $transaction_id }</code>

refund-error = 
    ❌ <b>Failed to refund payment</b>: <pre>{ $error }</pre>

amount-invalid = 
    ❌ <b>Invalid amount</b>
    
    Please send a whole number between <b>1</b> and <b>100000</b>.
    
    ℹ️ Example: <code>150</code>

balance-info = 
    💰 <b>Bot (@{ $username }) balance</b>: { $amount }⭐️

payment-link = <b>Payment link:</b> <a href="{ $link }">{ $link }</a>

refund-success = ✅ <b>Payment has been successfully refunded!</b>

invoice-description = Payment for services via Stars.

invoice-error = ❌ <b>Failed to create payment invoice</b>

invoice-label = Stars Payment

invoice-title = Stars Payment Example
