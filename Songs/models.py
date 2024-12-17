from django.db import models
from Albums.models import Albums 

class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name="songs") 
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    release_date = models.DateField()
    
    def __str__(self):
        return f"{self.title} ({self.album.title})"
