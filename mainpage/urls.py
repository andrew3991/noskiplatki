from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='PostList'),
	url(r'^contact/$', views.contact, name='contact'),
]
