#django
from django.db import models

class ImagesProfile(models.Model):
    # no need to set storage, field will use the default one
    image = models.ImageField(upload_to='images/profile/imgs_extra', blank=True)  