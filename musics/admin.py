from django.contrib import admin
from .models import Album, Song, Comment

# Register your models here.
@admin.register(Album)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'musician', 'is_public', 'updated_at']
    list_display_links = ['title']
    list_editable = ['is_public']

admin.site.register(Song)
admin.site.register(Comment)