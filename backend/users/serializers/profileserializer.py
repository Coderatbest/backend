# Django REST Framework
from rest_framework import serializers

# Models
from users.models.users import User
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    name= serializers.SerializerMethodField()
    age= serializers.SerializerMethodField()
    biography= serializers.SerializerMethodField()

    def get_name(self,obj:User):
        return f'{obj.first_name.capitalize()} {obj.last_name.capitalize()}'
    def get_biography(self,obj:User):
        profile= Profile.objects.filter(user=obj).first()
        return profile.biography.split('\n')
    def get_age(self,obj:User):
        profile= Profile.objects.filter(user=obj).first()
        return profile.age
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['name','age','biography','last_login']
        # exclude = ['id']