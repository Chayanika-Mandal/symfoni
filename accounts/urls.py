from django.urls import path

from accounts.views import UserCreateView, UserLoginView, UserLogoutView

app_name = "accounts"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
