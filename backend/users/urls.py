#django
from django.urls import path,include
# rest frameworks
from rest_framework.routers import DefaultRouter
# models
from users import views as user_views


router = DefaultRouter()

router.register(r'auth',user_views.UsersViewSet,basename='auth')

urlpatterns = [
    path('',include(router.urls))
]