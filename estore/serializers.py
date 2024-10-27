from rest_framework import serializers
from estore.models import category, product

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'