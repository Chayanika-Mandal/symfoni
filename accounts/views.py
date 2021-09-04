from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


# Create your views here.


class UserCreateView(CreateView):
    template_name = "accounts/register.html"
    model = User
    fields = ["username", "password", "first_name", "last_name", "email"]
    success_url = reverse_lazy("home_page")
