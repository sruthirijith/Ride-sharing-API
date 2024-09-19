

from django.contrib import admin
from .models import Profile  # Ensure this imports your Profile model

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_driver')  # Customize this as needed
