from django.contrib import admin
from django.contrib.admin.decorators import register

from django.contrib.auth.admin import UserAdmin

from users.models import User,Profile,ImagesProfile
from commentaries.models import CommentariesModels
from posts.models import PostsModels
from visits.models import VisitsModels


class ImagesProfileInline(admin.TabularInline):
    model = ImagesProfile
class customUserAdmin(UserAdmin):
    """
    docs.
    """
    list_display=('username','email', 'first_name','last_name','is_staff','is_verified','user_created','date_created')
    list_filter = ('is_client','is_staff','date_created','date_modified')
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    docs.
    """
    list_display=('user','age')
    inlines = [
        ImagesProfileInline,
    ]
    ordering=['id']

@admin.register(CommentariesModels)
class CommentariesAdmin(admin.ModelAdmin):
    """
    docs.
    """
    list_display=('body','answers_to','user_created','date_created')
    
    ordering=['date_created']
@admin.register(PostsModels)
class PostsAdmin(admin.ModelAdmin):
    """
    docs.
    """
    list_display=('title','content','valid_date','user_created','date_created')
    
    ordering=['date_created']
@admin.register(VisitsModels)
class VisitsAdmin(admin.ModelAdmin):
    """
    docs.
    """
    list_display=('ip_adreess','user_created','date_created')
    
    ordering=['date_created']


admin.site.register(User,customUserAdmin)