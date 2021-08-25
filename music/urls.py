from django.urls import path, include
from music.views import home_page

urlpatterns = [
    path("", home_page, name="home_page"),
]
