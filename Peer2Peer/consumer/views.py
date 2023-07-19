from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from .models import Products
from .serializers import ListProductSerializer

class ListProducts(APIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer



