from django.db import models
from utilies.models import defaultModels

class VisitsModels(defaultModels):
    """
    Docs.
    """
    ip_adreess=models.TextField(
        max_length=70,
        unique=True
    )