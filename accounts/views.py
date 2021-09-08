from accounts.forms import RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()


# Create your views here.


class UserCreateView(CreateView):
    template_name = "accounts/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("home_page")


class UserLoginView(LoginView):
    template_name = "accounts/login.html"


class UserLogoutView(LogoutView):
    template_name = "accounts/logout.html"
