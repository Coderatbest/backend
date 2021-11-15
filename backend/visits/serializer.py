#django rest frameworks
from rest_framework import serializers
# models 
from visits.models import VisitsModels

class CommentariesModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VisitsModels
        fields = (
            'id',
            'user_created',
            'date_created',
            'ip_adreess',
        )