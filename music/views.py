from django.shortcuts import render

from music.models import Artist


def all_songs(request):
    return render(request, "music/all-songs.html")


def all_artists(request):
    context_dictionary = {"artists": Artist.objects.all()}
    return render(request, "music/all-artists.html", context_dictionary)
