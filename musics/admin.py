from django.contrib import admin
from .models import Album, Song, Comment

# Register your models here.
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