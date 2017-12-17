from django.conf.urls import include, url
from . import views
from .models import ProductLike
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/', views.EProductView.as_view(), name='ProductDetail'),
	url(r'^comment/(?P<id>\d+)/$', views.add_comment, name='add_comment'),
	url(r'^search/$', views.search, name='search'),
	url(r'^products/', views.ProductList, name='ProductList'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/new/$', views.like_product, name='like_product'),

]




	# url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/', include([
	# 	url(r'^', views.EProductView.as_view(), name='ProductDetail'),
	# 	url(r'comment/$', views.add_comment, name='add_comment'),
	# ])),