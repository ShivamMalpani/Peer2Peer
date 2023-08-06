from django.urls import include, path
from rest_framework import routers
from .views import *
from django.contrib import admin
router = routers.DefaultRouter()
# router.register(r'products', )

urlpatterns = [
    path('product/<int:pk>/', ViewUpdateDeleteProducts.as_view(),name='view_products'),
    path('products_list/', ListCreateProducts.as_view(), name='list_products'),
    path('cart/<str:userID>/',ViewDeleteCart.as_view(),name='cart'),
    path('insert_cart/', InsertToCart.as_view(), name='insert_cart'),
    path('container/<str:id>/', ViewCreateContainer.as_view(), name='container'),
    path('reviews/<str:product>/', ListCreateReviews.as_view(), name='reviews'),
    path('ratings/<str:product>/<str:userID>/<int:rate>/', ViewUpdateRatings.as_view(), name='ratings'),
    path('average_rating/<str:product>/', ListRatings.as_view(), name='rate'),
    path('coupon/', Coupons.as_view(), name='coupon'),
]