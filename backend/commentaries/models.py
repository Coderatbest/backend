from django.db import models
from utilies.models import defaultModels

class CommentariesModels(defaultModels):
    """
    Docs.
    """
    body=models.TextField(
        max_length=70,
    )
    answers_to= models.ForeignKey(
        "commentaries.CommentariesModels", 
        on_delete=models.CASCADE,
        null=True,
        related_name='%(app_label)s_%(class)s_answers_to'
    )