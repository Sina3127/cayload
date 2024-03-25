from django.urls import path

from track.views import Tracker

urlpatterns = [
    path('', Tracker.as_view(), name='tracker'),
]