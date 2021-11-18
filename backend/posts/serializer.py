#django rest frameworks
from rest_framework import serializers
# models 
from posts.models import PostsModels

class PostsModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostsModels
        fields = (
            'id',
            'title',
            'content',
            'valid_date',
            'user_created',
            'date_created',
        )