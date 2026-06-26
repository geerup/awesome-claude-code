# Failed-payment recovery email (production copy, mined)

Source: [Failed Payments Copy](https://docs.google.com/document/d/1PPCKu-90yZr0owIPdx_9IisUV9Ptnstpkr1G3q_q3YI/edit)
(00- Maharat / 07, 2024). The team's live bilingual recovery email. Pairs with user
list 1 (Failed Payments, 2-hour window) in segmentation-logic/templates/maharat-user-lists.md.
Extracted 2026-06-04.

## Structure (keep)
Subject names the problem plainly (Payment Issue on Maharat). Empathy line, then three
numbered actions: try another payment method, contact your bank (security declines),
reach support (address given, reply-to works). Warm close pointing forward to the
classes. Same structure in EN and AR.

## Register note
The AR is formal MSA (plural courtesy form). This is the transactional register: see
the register-precedents note in email-copy/templates/tpay-egypt-announcement.md.

## Cleaned renders (house style; the source AR has a typo, "بطاقة أو مختلفة")
- AR action 1 render: تجربة وسيلة دفع أخرى: ننصحكم بتجربة بطاقة مختلفة أو وسيلة دفع أخرى.
- Add when relevant (post-TPAY, Egypt): الدفع عبر المحافظ الإلكترونية متاح أيضا.

## Adaptation rules
- Keep one job per email: recover the payment. No upsell in this email.
- The 2-hour window from the list spec is the send trigger; one send, then the user
  exits on purchase.
- Support address and reply-to behavior are facts to keep current (support@maharat.com
  as of the source).
