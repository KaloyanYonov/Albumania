from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Albums
from .forms import AlbumForm
from Songs.models import Song 


def album_list(request):
    albums = Albums.objects.all()
    return render(request, 'Albums/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    songs = album.songs.all() 
    return render(request, 'Albums/album_detail.html', {'album': album, 'songs': songs})


@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.created_by = request.user
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'Albums/add_album.html', {'form': form})

@login_required
def edit_album(request, pk):
    album = get_object_or_404(Albums, pk=pk) 
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', pk=album.pk) 
    else:
        form = AlbumForm(instance=album)
    return render(request, 'Albums/edit_album.html', {'form': form, 'album': album})

@login_required
def delete_album(request, pk):
    album = get_object_or_404(Albums, pk=pk, created_by=request.user)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'Albums/delete_album.html', {'album': album})
