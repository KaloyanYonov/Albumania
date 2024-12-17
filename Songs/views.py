from django.shortcuts import get_object_or_404, redirect, render
from .models import Song
from .forms import SongForm
from Albums.models import Albums

# Add a new song
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
    return render(request, 'Songs/song_list.html', {'album': album, 'songs': songs})
