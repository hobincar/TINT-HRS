from django.conf.urls import url
from .views import reserve, modify


urlpatterns = [
    url(r'^modify/$', modify, name='modify'),
    url(r'^$', reserve, name='reserve'),
]
