# ecommerceapp

Payment gateway flowchart:

1. User goes to Frontend (e.g., Amazon, searches products)
2. Frontend calls Order Service
3. Order Service creates order in DB and returns Order ID
4. Frontend calls Payment Service with Order ID
5. Payment Service calls Order Service to get amount for Order ID
6. Payment Service sends Order ID + Amount to Razorpay
7. Razorpay generates unique payment URL
8. Payment Service returns URL to Frontend
9. Frontend redirects user to Razorpay payment page
10. User makes payment on Razorpay page
11. Razorpay calls Payment Service webhook
12. Payment Service re-verifies with Razorpay if payment really done
13. Razorpay confirms payment status
14. Payment Service calls Order Service
15. Order Service updates order status (success/failed)

Key points:
Webhook (step 11) is more reliable than callback as it's server-to-server
Re-verification in step 12 prevents fraud
Order created first, then payment initiated

#https://www.google.com/?razorpay_payment_id=pay_PJx2PNJL2P3Wdo&razorpay_payment_link_id=plink_PJwy4QAAIHlFDX&razorpay_payment_link_reference_id=&razorpay_payment_link_status=paid&razorpay_signature=e97dda2a78bac4ea9e8ea44b08fb25019500e1b116c6535c1e6dea8208084338