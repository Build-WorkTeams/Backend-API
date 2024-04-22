from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import (
    RegisterSerializer as DJRegisterSerializer,
)
from dj_rest_auth.serializers import (
    LoginSerializer as DJLoginSerializer,
    UserDetailsSerializer as DJUserDetailsSerializer,
    PasswordChangeSerializer as DJPasswordChangeSerializer,
)


class RegisterSerializer(DJRegisterSerializer):
    username = None
    password = serializers.CharField(write_only=True)
    password1 = None
    password2 = None

    def validate(self, data):
        data["password1"] = data["password"]
        return data

    def validate_email(self, email):
        email = super().validate_email(email)
        if get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "A user is already registered with this e-mail address."
            )
        return email

    def validate_password(self, password):
        return super().validate_password1(password)

    def get_cleaned_data(self):
        return self.validated_data


class LoginSerializer(DJLoginSerializer):
    username = None


class UserDetailsSerializer(DJUserDetailsSerializer):
    class Meta(DJUserDetailsSerializer.Meta):
        fields = ["email"]  # noqa: F811


class PasswordChangeSerializer(DJPasswordChangeSerializer):
    new_password = serializers.CharField(write_only=True)
    new_password1 = None
    new_password2 = None
