# Django REST Framework
from rest_framework import serializers

# Models
from users.models import ImagesProfile, Profile


class ProfileSerializer(serializers.ModelSerializer):
    name= serializers.SerializerMethodField()
    last_login= serializers.SerializerMethodField()
    biography= serializers.SerializerMethodField()
    imgs_extra = serializers.SerializerMethodField()

    def get_name(self,obj):
        return f'{obj.user.first_name.capitalize()} {obj.user.last_name.capitalize()}'
    def get_last_login(self,obj):
        return obj.user.last_login
    def get_biography(self,obj):
        return obj.biography.split('\n')
    def get_imgs_extra(self,obj):
        queryset =ImagesProfile.objects.filter(profile=obj)
        images = [ image.image.url for image in queryset]
        return images
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ['name','age','imgs_extra','biography','image','last_login']
        # exclude = ['id']