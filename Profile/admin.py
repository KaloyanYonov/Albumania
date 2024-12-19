from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_genre', 'preferred_criteria')  
    list_filter = ('favorite_genre', 'preferred_criteria')  
    search_fields = ('user__username',)  
    ordering = ('user',) 
