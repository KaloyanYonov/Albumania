from django.urls import path
from . import views

urlpatterns = [
    path('album/<int:album_id>/rank/', views.rank_album, name='rank_album'),
    path('song/<int:song_id>/rank/', views.rank_song, name='rank_song'),
]
