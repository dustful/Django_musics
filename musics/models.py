from django.db import models
from django.conf import settings

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length = 100)
    musician = models.CharField(max_length = 50)
    cover = models.ImageField()
    release_at = models.DateTimeField()
    genre = models.CharField(max_length = 20)
    distribution = models.CharField(max_length = 20)
    introduction = models.TextField()
    is_public = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    musician = models.CharField(max_length = 50)
    order = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.message