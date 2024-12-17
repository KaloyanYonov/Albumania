from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_genre', 'preferred_criteria')

    list_filter = ('favorite_genre', 'preferred_criteria')

    search_fields = ('user__username', 'user__email')

    fields = ('user', 'profile_picture', 'favorite_genre', 'preferred_criteria')

admin.site.register(Profile, ProfileAdmin)
