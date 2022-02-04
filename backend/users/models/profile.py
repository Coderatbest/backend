#django
from django.db import models

class Profile(models.Model):
    """docs."""
    user = models.OneToOneField('users.User',on_delete=models.CASCADE)
    image = models.ImageField(
        'profile picture',
        upload_to='images/users/profile/',
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(
        null=True
    )
    # imgs =  
    biography = models.TextField(max_length=2000, blank=True)