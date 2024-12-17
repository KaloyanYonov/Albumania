from django.db import models
from django.contrib.auth.models import User

GENRE_CHOICES = [
    ('Pop', 'Pop'),
    ('Rock', 'Rock'),
    ('Classical', 'Classical'),
    ('Rap', 'Rap'),
    ('Jazz', 'Jazz'),
    ('Electronic', 'Electronic'),
    ('Metal', 'Metal'),
    ('Country', 'Country'),
]

class Albums(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    cover_image = models.URLField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f"{self.name} by {self.artist}"
