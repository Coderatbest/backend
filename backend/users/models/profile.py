#django
from django.db import models
#models
from users.models.images import ImagesProfile

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

    imgs_extra = models.ForeignKey(
        to=ImagesProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )