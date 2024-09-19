from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RideViewSet

router = DefaultRouter()
router.register(r'', RideViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
