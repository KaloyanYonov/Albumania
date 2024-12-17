from django import forms
from .models import Albums

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums

        fields = ['name', 'artist', 'release_date', 'genre', 'cover_image']
