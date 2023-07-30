from django.urls import include, path
from rest_framework import routers
from .views import ViewUpdateDeleteProducts,ListCreateProducts, ViewUpdateCart
from django.contrib import admin
router = routers.DefaultRouter()
# router.register(r'products', )

urlpatterns = [
    path('product/<int:pk>/', ViewUpdateDeleteProducts.as_view(),name='view_products'),
    path('products_list/', ListCreateProducts.as_view(), name='list_products'),
    path('cart/<str:pk>/',ViewUpdateCart.as_view(),name='cart')
]