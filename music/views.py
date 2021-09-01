from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from music.forms import ArtistForm
from music.models import Artist, Song


def all_songs(request):
    context_dictionary = {"songs": Song.objects.all()}
    return render(request, "music/all-songs.html", context_dictionary)


class AllArtistView(TemplateView):
    template_name = "music/all-artists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artists"] = Artist.objects.all()
        return context


# class AddArtistView(CreateView):
#     template_name = "music/add-artist.html"
#     model = Artist
#     fields = ["name"]
#     success_url = "/music/all-artists"


def add_artist_view(request):
    if request.method == "GET":
        print("request-method: ", request.method)
        form = ArtistForm()
        return render(request, "music/add-artist.html", {"form": form})
    artist_name = request.POST["name"]
    artist = Artist.objects.create(name=artist_name)
    artist.save()
    return redirect(reverse("music:all_artists"))
