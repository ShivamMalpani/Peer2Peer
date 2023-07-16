from django.urls import include, path
from rest_framework import routers
# from .views import
from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'products', )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]