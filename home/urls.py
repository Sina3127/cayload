
from django.urls import path

from home.views import Home, AboutPage, ServicePage, Contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('service/', ServicePage.as_view(), name='service'),
    path('contact/', Contact.as_view(), name='contact'),
]