
# Django REST Framework
from rest_framework import serializers

# Models
from users.models import ImagesProfile


class ImagesExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesProfile
        # fields = '__all__'
        fields = ['image',]
        # exclude = ['id']