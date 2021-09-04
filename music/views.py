from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from music.models import Artist, Song


class ListSongView(ListView):
    template_name = "music/all-songs.html"
    model = Song


class ListArtistView(ListView):
    template_name = "music/all-artists.html"
    model = Artist


class CreateArtistView(CreateView):
    template_name = "music/add-artist.html"
    model = Artist
    fields = ["name"]
    success_url = reverse_lazy("music:all_artists")


class CreateSongView(CreateView):
    template_name = "music/add-song.html"
    model = Song
    fields = ["name", "url", "artist"]
    success_url = reverse_lazy("music:all_songs")


# def add_artist_view(request):  # function based view
#     if request.method == "GET":
#         print("request-method: ", request.method)
#         form = ArtistForm()
#         return render(request, "music/add-artist.html", {"form": form})
#     artist_name = request.POST["name"]
#     artist = Artist.objects.create(name=artist_name)
#     artist.save()
#     return redirect(reverse("music:all_artists"))
