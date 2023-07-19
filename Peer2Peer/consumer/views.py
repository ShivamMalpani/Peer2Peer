from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from .models import Products
from .serializers import ListProductSerializer

class ViewUpdateDeleteProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer
    def update(self, request, *args, **kwargs):
        # return Response here
        pass





