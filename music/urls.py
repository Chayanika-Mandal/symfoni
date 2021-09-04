from django.urls import path

from music.views import CreateArtistView, CreateSongView, ListArtistView, ListSongView

app_name = "music"

urlpatterns = [
    path("all-songs/", ListSongView.as_view(), name="all_songs"),
    path("all-artists/", ListArtistView.as_view(), name="all_artists"),
    path("add-artist/", CreateArtistView.as_view(), name="add_artist"),
    path("add-song/", CreateSongView.as_view(), name="add_song"),
]
