from rest_framework import serializers
from .models import Products, User

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
