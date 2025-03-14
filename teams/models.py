from django.db import models
from users.models import CustomUser

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(CustomUser, related_name='teams')

    class Meta:
        app_label = 'teams'  # App label ni aniqlash