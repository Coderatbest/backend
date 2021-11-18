#django
from django.urls import path,include
# rest frameworks
from rest_framework.routers import DefaultRouter
# models
from posts import views as posts_viewset


router = DefaultRouter()

router.register(r'posts',posts_viewset.PostsViewSets,basename='auth')

urlpatterns = [
    path('',include(router.urls))
]