from payment.gateways.payment_gateways import RazorpayGateway


class PaymentService:
    def __init__(self):
        self.payment_gateway = RazorpayGateway()
    def initiate_payment(self, order_id, amount):
        return self.payment_gateway.generate_payment_link(order_id,amount)