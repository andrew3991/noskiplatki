from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^news/$', views.PostNewsList, name='PostNewsList'),
	url(r'^news/(?P<id>\d+)/$', views.PostNewsDetail, name='PostNewsDetail'),
]