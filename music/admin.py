from django.contrib import admin

# Register your models here.

from music.models import Artist, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
