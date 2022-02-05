
# Django REST Framework
from rest_framework import serializers

# Models
from users.models import TimeLineProfile


class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLineProfile
        # fields = '__all__'
        fields = ('year','comment','icon','profile')
        # exclude = ['id']