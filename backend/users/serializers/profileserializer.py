# Django REST Framework
from rest_framework import serializers
#serialiezers
from users.serializers.time_line_serialiezer import TimeLineSerializer
from users.serializers.images_extra_serialiezer import ImagesExtraSerializer
# Models
from users.models import Profile,ImagesProfile,TimeLineProfile


class ProfileSerializer(serializers.ModelSerializer):
    name= serializers.SerializerMethodField()
    last_login= serializers.SerializerMethodField()
    biography= serializers.SerializerMethodField()
    
    images_profile = serializers.StringRelatedField(many=True,read_only=True)
    time_line_profile = TimeLineSerializer(many=True)

    def get_name(self,obj):
        return f'{obj.user.first_name.capitalize()} {obj.user.last_name.capitalize()}'
    def get_last_login(self,obj):
        return obj.user.last_login
    def get_biography(self,obj):
        return obj.biography.split('\n')
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = [
            'name',
            'age',
            'biography',
            'image',
            'images_profile',
            'time_line_profile',
            'last_login'
        ]
        # exclude = ['id']