#django rest frameworks
from rest_framework import serializers
# models 
from commentaries.models import CommentariesModels

class CommentariesModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentariesModels
        fields = (
            'id',
            'user_created',
            'date_created',
            'body',
        )