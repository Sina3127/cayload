
from django.urls import path

from home.views import Home, Tracker

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("tracker/", Tracker.as_view(), name='tracker')
]