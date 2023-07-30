from django.urls import include, path
from rest_framework import routers
from .views import *
from django.contrib import admin
router = routers.DefaultRouter()
# router.register(r'products', )

urlpatterns = [
    path('product/<int:pk>/', ViewUpdateDeleteProducts.as_view(),name='view_products'),
    path('products_list/', ListCreateProducts.as_view(), name='list_products'),
    path('cart/<str:userID>/',ViewUpdateCart.as_view(),name='cart'),
    path('insert_cart/', InsertToCart.as_view(), name='cart'),
]