from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from utilies.models import defaultModels

class User(defaultModels,AbstractUser):
    """
    Docs.
    """
    email= models.EmailField(
        'email address',
        unique=True,
        max_length=40,
        error_messages={
            'unique':'a user with'
        }
    )

    phone_regex= RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='format +999999999.'
    )
    phone_number=models.CharField(validators=[phone_regex],max_length=17, blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    is_client=models.BooleanField(
        'client status',
        default=True,
        help_text='diference client and admin'
    )
    is_verified=models.BooleanField(
        'verified status',
        default=False,
    )

    user_created = models.ForeignKey("users.User", on_delete=models.CASCADE,null=True,related_name='creator')
    user_modified = models.ForeignKey("users.User", on_delete=models.CASCADE,null=True,related_name='modificator')

    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username