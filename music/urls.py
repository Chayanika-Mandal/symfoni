from django.urls import path

from music.views import AllArtistView, add_artist_view, all_songs

app_name = "music"

urlpatterns = [
    path("all-songs/", all_songs, name="all_songs"),
    path("all-artists/", AllArtistView.as_view(), name="all_artists"),
    path("add-artist/", add_artist_view, name="add_artist"),
]
