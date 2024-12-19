from django.db import models

class Song(models.Model):
    album = models.ForeignKey('Albums.Albums', on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    lyrics = models.TextField(blank=True, null=True)

    def get_final_score(self, user):
        from Ranking.models import Ranking
        ranking = Ranking.objects.filter(song=self, user=user).first()
        if ranking:
            return ranking.calculate_final_score(user.profile.preferred_criteria)
        return "N/A"


    def __str__(self):
        return f"{self.title} ({self.album.name})"
