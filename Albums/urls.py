from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('<int:pk>/', views.album_detail, name='album_detail'),
    path('add/', views.add_album, name='add_album'),
    path('<int:pk>/edit/', views.edit_album, name='edit_album'),
    path('<int:pk>/delete/', views.delete_album, name='delete_album'),
]
