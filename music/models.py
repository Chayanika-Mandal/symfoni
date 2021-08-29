from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Artist(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"Artist named {self.name}"


class Song(models.Model):
    name = models.CharField(max_length=50, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField()
    users_who_liked = models.ManyToManyField(
        User, related_name="users_who_liked", blank=True
    )

    def __str__(self) -> str:
        if self.artist:
            return f"{self.name} by {self.artist.name}"
        return f"{self.name}"
