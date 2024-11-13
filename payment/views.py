from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from payment.serializers import PaymentSerializer
from payment.service import PaymentService


# Create your views here.

class PaymentView(APIView):
    def __init__(self):
        super().__init__()
        self.service = PaymentService()

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data.get('order_id')
            amount = serializer.validated_data.get('amount')
            try:
                payment_link = self.service.initiate_payment(order_id, amount)
                return Response({'payment_link': payment_link}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

