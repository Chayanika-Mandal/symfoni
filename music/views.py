from django.shortcuts import render

from music.models import Artist, Song


def all_songs(request):
    context_dictionary = {"songs": Song.objects.all()}
    return render(request, "music/all-songs.html", context_dictionary)


def all_artists(request):
    context_dictionary = {"artists": Artist.objects.all()}
    return render(request, "music/all-artists.html", context_dictionary)
