from django.conf.urls import url

from . import views

app_name = 'search'
urlpatterns = [
    url(r'^productsearch/$', views.ESearchView.as_view(), name='productsearch'),
]