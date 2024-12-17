from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.profile_dashboard, name='profile_dashboard'),
]
