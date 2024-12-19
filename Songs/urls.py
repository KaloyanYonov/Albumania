from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.song_detail, name='song_detail'),  
    path('<int:pk>/edit/', views.edit_song, name='edit_song'),
    path('<int:pk>/delete/', views.delete_song, name='delete_song'),
    path('<int:album_id>/add/', views.add_song, name='add_song'),
    path('<int:album_id>/', views.song_list, name='song_list'), 
]
