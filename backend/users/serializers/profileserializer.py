# Django REST Framework
from rest_framework import serializers

# Models
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #fields = '__all__'
        exclude = ['id']