from django.db import models
from utilies.models import defaultModels

class Commentaries(defaultModels):
    """
    Docs.
    """
    body=models.TextField(
        max_length=70,
    )