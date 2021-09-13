from django.contrib.auth import get_user_model
from django.db import models
from uuid import uuid4

User = get_user_model()


class Artist(models.Model):
    name = models.CharField(max_length=50, null=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Artist named {self.name}"


class Song(models.Model):
    name = models.CharField(max_length=50, null=False)
    artists = models.ManyToManyField(Artist, related_name="artists", blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    users_who_liked = models.ManyToManyField(
        User, related_name="users_who_liked", blank=True
    )

    def __str__(self) -> str:
        if self.artists.count() == 0:
            return self.name
        artists_names = map(lambda s: s.name, self.artists.all())
        names = ", ".join(artists_names)
        return f"{self.name} by {names}"


class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=75, null=False)
    songs = models.ManyToManyField(Song, related_name="songs", blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        if self.songs.count() == 0:
            return self.name
        song_names = map(lambda s: s.name, self.songs.all())
        names = ", ".join(song_names)
        return f"{self.name} containing {names}"
