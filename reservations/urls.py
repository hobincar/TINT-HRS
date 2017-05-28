from django.conf.urls import url
from .views import reserve


urlpatterns = [
    url(r'', reserve, name='reserve'),
]
