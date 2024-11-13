import json
from abc import ABC, abstractmethod
import razorpay

from ecommerceApp import settings


class PaymentGateway(ABC):
    @abstractmethod
    def generate_payment_link(self, order_id, amount):
        pass

class RazorpayGateway(PaymentGateway):
    def __init__(self):
        self.client = razorpay.Client(
            auth=(settings.RAZORPAY_ID, settings.RAZORPAY_SECRET),
        )
    def generate_payment_link(self, order_id, amount):
        payment_data = {

            "amount": amount,
            "currency": "INR",
            "description": "For XYZ purpose",
            "customer": {
                "name": "Vinod",
                "email": "vinod.vinnu542@gmail.com",
                "contact": "+919494645182"
            },
            "notify": {
                "sms": True,
                "email": True
            },
            "reminder_enable": True,
            "callback_url": "https://google.com/",
            "callback_method": "get"
        }
        payment_link = self.client.payment_link.create(payment_data)
        return json.dumps(payment_link)
