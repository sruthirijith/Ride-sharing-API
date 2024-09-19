from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomAuthToken, RegisterUserView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rides/', include('rides.urls')),  # rides URLs
    path('api/', include(router.urls)),         # users API
    path('api/login/', CustomAuthToken.as_view(), name='login'),  # login endpoint
    path('api/register/', RegisterUserView.as_view(), name='register'), 
]
