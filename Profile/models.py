from django.db import models
from django.contrib.auth.models import User

CRITERIA_CHOICES = [
    ('Lyricism', 'Lyricism'),
    ('Melody', 'Melody'),
    ('Instrumentals', 'Instrumentals'),
    ('Vocals', 'Vocals'),
]

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    favorite_genre = models.CharField(max_length=20, choices=GENRE_CHOICES, blank=True)
    preferred_criteria = models.CharField(max_length=20, choices=CRITERIA_CHOICES, default='Melody')

    def __str__(self):
        return f"{self.user.username}'s Profile"
