#django rest frameworks
from rest_framework import serializers
# models 
from posts.models import PostsModels

class CommentariesModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostsModels
        fields = (
            'id',
            'user_created',
            'date_created',
            'content',
        )