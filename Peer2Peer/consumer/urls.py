from django.urls import include, path
from rest_framework import routers
from .views import ViewUpdateDeleteProducts
from django.contrib import admin
router = routers.DefaultRouter()
# router.register(r'products', )

urlpatterns = [
    path('product/<int:pk>', ViewUpdateDeleteProducts.as_view(),name='list_products'),

]