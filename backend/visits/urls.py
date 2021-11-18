#django
from django.urls import path
# views
from visits.views import  VisitsViewSets

urlpatterns = [
    path('visits/',VisitsViewSets.as_view())
]