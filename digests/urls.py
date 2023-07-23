from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls))
]
