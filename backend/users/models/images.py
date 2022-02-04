#django
from django.db import models
#models
from users.models import Profile
class ImagesProfile(models.Model):
    # no need to set storage, field will use the default one
    image = models.ImageField(
        'extra image',
        upload_to='images/users/profile/imgs_extra',
        blank=True,
        null=True,
    )  

    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )