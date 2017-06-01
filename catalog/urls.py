from django.conf.urls import url
from . import views
from .models import ProductLike
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^search/$', views.search, name='search'),
	url(r'^products/', views.ProductList, name='ProductList'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/new/$', views.like_product, name='like_product'),
]