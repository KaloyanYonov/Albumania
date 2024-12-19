from django.db import models
from django.contrib.auth.models import User

class Ranking(models.Model):
    song = models.ForeignKey('Songs.Song', on_delete=models.CASCADE, related_name='rankings', null=True, blank=True)
    album = models.ForeignKey('Albums.Albums', on_delete=models.CASCADE, related_name='rankings', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    melody = models.IntegerField(default=0)
    instrumentals = models.IntegerField(default=0)
    vocals = models.IntegerField(default=0)
    lyricism = models.IntegerField(default=0)

    def calculate_final_score(self, preferred_criteria, weight_favorite=3, weight_others=1):
        favorite_score = getattr(self, preferred_criteria, 0)
        
        all_scores = {
            'melody': self.melody,
            'instrumentals': self.instrumentals,
            'vocals': self.vocals,
            'lyricism': self.lyricism,
        }
        
        other_scores = [
            score for key, score in all_scores.items() if key != preferred_criteria
        ]
        
        weighted_score = (
            (weight_favorite * favorite_score) +
            (weight_others * sum(other_scores))
        ) / (weight_favorite + (weight_others * len(other_scores)))
        
        return round(weighted_score, 2)

    def __str__(self):
        return f"Ranking by {self.user.username}"
