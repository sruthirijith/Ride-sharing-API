from rest_framework import serializers
from django.contrib.auth.models import User
from rides.models import Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_driver = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_driver', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def get_is_driver(self, obj):
        # Access is_driver from the related Profile model
        return getattr(obj.profile, 'is_driver', None)  # Safely get is_driver or None if no profile

    def validate_email(self, value):
        """Check if the email is already registered."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def create(self, validated_data):
        is_driver = validated_data.pop('is_driver', False)  # Extract is_driver from validated_data
        password = validated_data.pop('password')  # Extract password to set later
        
        # Create the user instance
        user = User(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()

        # Use get_or_create to ensure no duplicate profile is created
        Profile.objects.get_or_create(user=user, defaults={'is_driver': is_driver})

        return user