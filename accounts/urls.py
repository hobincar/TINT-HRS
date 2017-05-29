from django.conf.urls import url
from .views import register, login, logout, mypage


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^mypage/$', mypage, name='mypage'),
]
