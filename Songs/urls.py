from django.urls import path
from . import views

urlpatterns = [
    path('<int:album_id>/add/', views.add_song, name='add_song'), 
    path('<int:album_id>/', views.song_list, name='song_list'),
]
