from django.conf.urls import url
from .views import reserve, modify, cancel


urlpatterns = [
    url(r'^modify/$', modify, name='modify'),
    url(r'^cancel/$', cancel, name='cancel_reservation'),
    url(r'^$', reserve, name='reserve'),
]
