from django.conf.urls import url
from .views import reservation


urlpatterns = [
    url(r'', reservation, name='reservations'),
    url(r'^add/$', reservation, name='reserve'),
]
