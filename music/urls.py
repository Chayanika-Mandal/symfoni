from django.urls import path

from music.views import all_artists, all_songs

urlpatterns = [
    path("all-artists/", all_artists, name="all_artists"),
    path("all-songs/", all_songs, name="all_songs"),
]
