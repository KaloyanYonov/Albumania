from django.shortcuts import get_object_or_404, redirect, render
from .models import Song
from .forms import SongForm
from Albums.models import Albums

def add_song(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album 
            song.save()
            return redirect('album_detail', pk=album_id)
    else:
        form = SongForm(initial={'album': album})
    return render(request, 'Songs/add_song.html', {'form': form, 'album': album})


def song_list(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    songs = album.songs.all()
    for song in songs:
        if request.user.is_authenticated:
            song.final_score = song.get_final_score(request.user)
        else:
            song.final_score = "N/A"
    return render(request, 'Songs/song_list.html', {'album': album, 'songs': songs})




def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    final_score = "N/A"
    if request.user.is_authenticated:
        final_score = song.get_final_score(request.user)
    return render(request, 'Songs/song_detail.html', {'song': song, 'final_score': final_score})


def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'Songs/edit_song.html', {'form': form, 'song': song})


def delete_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.delete()
    return redirect('album_detail', pk=song.album.pk)