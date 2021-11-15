from django.db import models

from django.db import models
from utilies.models import defaultModels

class PostsModels(defaultModels):
    """
    Docs.
    """
    content=models.TextField(
        max_length=70,
    )
    valid_date=models.DateField()