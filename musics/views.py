from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Song, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

# Create your views here.
def list(request):
    albums = Album.objects.all()
    context = {'albums' : albums}
    return render(request, 'musics/list.html', context)

def detail(request, id):
    album = Album.objects.get(id = id)
    songs = Song.objects.filter(album = id)
    # comments = Comment.objects.all().order_by('-id')[:10]
    comments = Comment.objects.filter(album = id)
    form = CommentForm()
    context = {
        'album' : album,
        'songs' : songs,
        'comments' : comments,
        'form' : form,
    }
    return render(request, 'musics/detail.html', context)

@login_required
def save_comment(request, id):
    # album = get_object_or_404(Album, pk = id)
    album = Album.objects.get(id = id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.album = album
            comment.user = request.user
            comment.save()
            return redirect('musics:detail', album.pk)
    else:
        form = CommentForm()
    return render(request, 'musics/detail.html', {'form' : form})