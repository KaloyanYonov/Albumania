from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_criteria = models.CharField(
        max_length=50,
        choices=[
            ('lyrics', 'Lyrics'),
            ('melody', 'Melody'),
            ('instrumentals', 'Instrumentals'),
            ('vocals', 'Vocals'),
        ],
        default='melody'
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
