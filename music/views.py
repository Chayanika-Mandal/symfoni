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

    def form_valid(self, form, *args, **kwargs):
        # artist = Artist.objects.create(
        #     name="qdwefsdgbgfnhjdwfsbg",
        #     artist="ed",
        #     added_by="Chayanika"
        # )
        # artist.save() # this is not called when you pass commit=False
        artist = form.save(commit=False)
        artist.added_by = self.request.user  # this is the currently logged in user
        artist.save()
        return super().form_valid(form, *args, **kwargs)


class CreateSongView(CreateView):
    template_name = "music/add-song.html"
    model = Song
    fields = ["name", "url", "artists"]
    success_url = reverse_lazy("music:all_songs")

    def form_valid(self, form, *args, **kwargs):
        # song = Song.objects.create(
        #     name="qdwefsdgbgfnhjdwfsbg",
        #     url="https://wM&usg=AOvVaw3",
        #     artist="ed",
        #     added_by="Chayanika"
        # )
        # song.save() # this is not called when you pass commit=False
        song = form.save(commit=False)
        song.added_by = self.request.user  # this is the currently logged in user
        song.save()
        return super().form_valid(form, *args, **kwargs)


# def add_artist_view(request):  # function based view
#     if request.method == "GET":
#         print("request-method: ", request.method)
#         form = ArtistForm()
#         return render(request, "music/add-artist.html", {"form": form})
#     artist_name = request.POST["name"]
#     artist = Artist.objects.create(name=artist_name)
#     artist.save()
#     return redirect(reverse("music:all_artists"))
