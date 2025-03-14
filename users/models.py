from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_participant = models.BooleanField(default=True)

    # groups va user_permissions maydonlarini qayta belgilash
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",  # Unique related_name
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",  # Unique related_name
        related_query_name="customuser",
    )

    class Meta:
        app_label = 'users'  # App label ni aniqlash