from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumRankingForm, SongRankingForm
from Albums.models import Albums
from Songs.models import Song
from .models import Ranking

def rank_album(request, album_id):
    album = get_object_or_404(Albums, id=album_id)
    if request.method == 'POST':
        form = AlbumRankingForm(request.POST)
        if form.is_valid():
            ranking = form.save(commit=False)
            ranking.user = request.user
            ranking.album = album
            ranking.save()
            return redirect('album_detail', pk=album_id)
    else:
        form = AlbumRankingForm()
    return render(request, 'Ranking/rank_album.html', {'form': form, 'album': album})

def rank_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongRankingForm(request.POST)
        if form.is_valid():
            ranking = form.save(commit=False)
            ranking.user = request.user
            ranking.song = song
            ranking.save()
            return redirect('song_detail', pk=song_id)
    else:
        form = SongRankingForm()
    return render(request, 'Ranking/rank_song.html', {'form': form, 'song': song})
