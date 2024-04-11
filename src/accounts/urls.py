from django.urls import path

from accounts.views import (
    LoginView,
    LogoutView, 
    LogoutAllView,
    RegisterView,
    UserView
)


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', LogoutAllView.as_view(), name='knox_logoutall'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name="user_detail"),  
]