#django
from django.db import models
#models
from users.models import Profile
class TimeLineProfile(models.Model):
    # no need to set storage, field will use the default one
    year = models.IntegerField(
        null=True,
        blank=False,
    )
    comment=models.CharField(
        max_length=300,
        null=True,
        blank=False
    )
    icon = models.CharField(
        max_length=20
    )

    profile = models.ForeignKey(
        related_name='time_line_profile',
        to=Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )