from django.contrib.auth import get_user_model, login
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.serializers import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from knox.views import LoginView as KnoxLoginView
from drf_spectacular.utils import extend_schema_view, extend_schema, inline_serializer

from .serializers import RegisterSerializer

User = get_user_model()

# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({"message": "Successfully created", "user": user.email}, 201)


@extend_schema_view(
    post=extend_schema(
        request=inline_serializer(name="Login", 
                                  fields={"email": serializers.EmailField(),
                                          "password": serializers.CharField()})
    )
)
class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return super(LoginView, self).post(request, format=None)
        return Response({"message": "Invalid Username/password"}, 401)
