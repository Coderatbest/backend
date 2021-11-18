#django rest frameworks
from rest_framework import serializers
# models 
from visits.models import VisitsModels

class VisitsModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VisitsModels
        fields = (
            'ip_adreess',
        )