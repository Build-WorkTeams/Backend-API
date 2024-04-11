from django.contrib.auth import get_user_model, login
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.authtoken.serializers import authenticate
from rest_framework import permissions
from rest_framework import generics
from knox.views import (
    LoginView as KnoxLoginView,
    LogoutView as KnoxLogoutView,
    LogoutAllView as KnoxLogoutAllView
)
from drf_spectacular.utils import extend_schema, inline_serializer

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
            responses={201: inline_serializer(name="RegisterResponse",
                                              fields={"message": serializers.CharField(),
                                                      "user": serializers.EmailField()}
                                            )
            }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({"message": "Successfully created", "user": user.email}, status.HTTP_201_CREATED)


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    @extend_schema(
        request=inline_serializer(name="Login", 
                                  fields={"email": serializers.EmailField(),
                                          "password": serializers.CharField()}),
        responses={200: inline_serializer(name="LoginResponse", 
                                          fields={"expiry": serializers.CharField(),
                                                  "token": serializers.CharField()}),
        }
    )
    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return super(LoginView, self).post(request, format=None)
        return Response({"message": "Invalid Username/password"}, 401)
    

class UserView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    extend_schema(
        responses={200: UserSerializer}
    )
    def get(self, request, *args, **kwargs):
        user = UserSerializer(request.user)
        return Response(user.data, status.HTTP_200_OK)
    

class LogoutView(KnoxLogoutView):
    
    @extend_schema(
            responses={204: None}
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)
    

class LogoutAllView(KnoxLogoutAllView):
    
    @extend_schema(
            responses={204: None}
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)
