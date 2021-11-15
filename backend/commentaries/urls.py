#django
from django.urls import path,include
# rest frameworks
from rest_framework.routers import DefaultRouter
# models
from commentaries import views as commentaries_viewset


router = DefaultRouter()

router.register(r'commentaries',commentaries_viewset.CommentariesViewSets,basename='auth')

urlpatterns = [
    path('',include(router.urls))
]