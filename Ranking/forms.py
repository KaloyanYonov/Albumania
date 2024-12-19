from django import forms
from .models import Ranking

class AlbumRankingForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ['melody', 'instrumentals', 'vocals', 'lyricism']

class SongRankingForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ['melody', 'instrumentals', 'vocals', 'lyricism']
