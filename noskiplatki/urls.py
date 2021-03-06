"""noskiplatki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from noskiplatki.sitemap import DinamicSitemap, StaticSitemap, CatalogSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {'articles': DinamicSitemap, 'static': StaticSitemap, 'catalog': CatalogSitemap}


urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('search.urls')),
    url(r'^', include('mainpage.urls', namespace='mainpage')),
    url(r'^', include('registr.urls')),
    url(r'^', include('news.urls', namespace='news')),
    url(r'^', include('catalog.urls', namespace='catalog')),
    url(r'^order/', include('orders.urls', namespace='orders')),
    url(r'^accounts/', include('user_profiles.urls', namespace='user_profiles')),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
