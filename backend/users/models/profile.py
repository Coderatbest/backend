from django.db import models

class Profile(models.Model):
    """docs."""
    user = models.OneToOneField('users.User',on_delete=models.CASCADE)
    image = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)