from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.profile_dashboard, name='profile_dashboard'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('login/', views.custom_login, name='custom_login'),
]
