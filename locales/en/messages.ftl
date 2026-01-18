start-intro = 
    ⭐️ <b>Telegram Stars Payment Demo Bot</b>
    
    This bot demonstrates <b>payment</b>, <b>refund</b>, and <b>balance</b> features with Telegram Stars.
    
    <b>How to pay:</b> use <code>/pay &lt;amount&gt;</code> (1 – 100000) to receive an invoice for that many ⭐️.
    
    <b>Refund:</b> Use <code>/refund &lt;user_id&gt; &lt;transaction_id&gt;</code> after a successful payment.
    <b>Balance:</b> Use <code>/balance</code> to view current Stars balance of the bot.
    <b>Paid media:</b> Use <code>/paid_media &lt;amount&gt;</code> (1 – 25000) with a photo.
    
    Send a payment command now to generate an invoice.

refund-invalid = 
    ❌ <b>Please use format:</b> /refund '&lt;user_id&gt;' '&lt;transaction_id&gt;'
    
    ℹ️ Example: <code>/refund 123456789 ABC123XYZ</code>

refund-default = 
    ❌ <b>Refund failed!</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    💭 <b>Error details:</b>
    <pre>{ $error }</pre>

refund-failed = 
    ❌ <b>Refund failed!</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ⚠️ The bot may have insufficient balance or a Telegram-side error occurred.

charge-already-refunded = 
    💰 <b>Refund already processed!</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ℹ️ This payment has already been refunded.

charge-not-found = 
    ❓ <b>Transaction not found!</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ⚠️ The specified transaction does not exist.

paid-media-invalid = 
    ❌ <b>Please use format:</b> /paid_media '&lt;amount&gt;'
    
    ℹ️ Example: <code>/paid_media 100</code>

refund-transactions-invalid = 
    ❌ <b>Please use format:</b> /refund_user '&lt;user_id&gt;'
    
    ℹ️ Example: <code>/refund_user 5616264938</code>

refund-transactions-summary = 
    ✅ <b>Refunds complete</b>
    
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    🔎 <b>Scanned:</b> { $scanned }
    ✅ <b>Refunded:</b> { $refunded }
    ⚠️ <b>Skipped:</b> { $skipped }

payment-success = 
    🎉 <b>Payment successful!</b>
    
    💵 <b>Amount:</b> { $amount }⭐️
    
    🆔 <b>Transaction ID:</b> <code>{ $transaction_id }</code>

refund-error = 
    ❌ <b>Failed to refund payment</b>: <pre>{ $error }</pre>

amount-invalid = 
    ❌ <b>Invalid amount!</b>
    
    Please send a whole number between <b>1</b> and <b>100000</b> using <code>/pay</code>.
    
    ℹ️ Example: <code>/pay 150</code>

balance-info = 
    💰 <b>Bot (@{ $username }) balance</b>: { $amount }⭐️

payment-link = <b>Payment link:</b> <a href="{ $link }">{ $link }</a>

refund-success = ✅ <b>Payment has been successfully refunded!</b>

invoice-error = ❌ <b>Failed to create payment invoice</b>: <pre>{ $error }</pre>

refund-transactions-error = ❌ <b>Failed to load transactions</b>: <pre>{ $error }</pre>

invoice-description = Payment for services via Stars.

invoice-label = Stars Payment

invoice-title = Stars Payment Example

paid-media-caption = 🔒 <b>Paid media</b>
