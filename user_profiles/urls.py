from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^profile/$', views.show_profile, name='show_profile'),
	url(r'^profile/about/$', views.show_profile_about, name='show_profile_about'),
	url(r'^profile/favorite/$', views.show_profile_favorites, name='show_profile_favorites'),
	url(r'^profile/edite/$', views.edite_profile, name='edite_profile'),
	url(r'^profile/favorite/(?P<product_id>\d+)/$', views.remove_like_product, name='remove_like_product'),
	url(r'^profile/orders/$', views.show_order_history, name='show_order_history'),
	url(r'^profile/orders/(?P<order_id>\d+)/$', views.show_order_history_detail, name='show_order_history_detail'),

]