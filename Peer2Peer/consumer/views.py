from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Products
from .serializers import ListProductSerializer

class ListProducts(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer