from django.contrib import admin
from django.urls import include, path

from symfoni.views import home_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("music/", include("music.urls")),
    path("", home_page, name="home_page"),
    path("accounts/", include("accounts.urls")),
]
