from django.contrib import admin
from .models import Albums

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'release_date', 'genre', 'created_by')
    list_filter = ('genre', 'release_date')
    search_fields = ('name', 'artist')
