from django.contrib import admin
from .models import Musician, Album, Song, Comment
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Musician)
# admin.site.register(Album)
# admin.site.register(Song)
# admin.site.register(Comment)
@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'agency']
    list_display_links = ['name']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'musician', 'is_public', 'updated_at']
    list_display_links = ['title']
    list_editable = ['is_public']
    list_filter = ['musician']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'album', 'order', 'title', 'musician', 'updated_at']
    list_display_links = ['title']
    list_editable = ['album', 'order']
    list_filter = ['album', 'musician']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'album', 'message', 'updated_at']
    list_display_links = ['message']