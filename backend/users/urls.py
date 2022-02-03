#django
from django.urls import path,include
# rest frameworks
from rest_framework.routers import DefaultRouter
# models
from users import views as user_views


router = DefaultRouter()

router.register(r'auth',user_views.UsersViewSet,basename='auth')
router.register(r'profile',user_views.ProfileViewSet,basename='profile')

urlpatterns = [
    path('',include(router.urls))
]