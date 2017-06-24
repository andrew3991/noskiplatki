from django.contrib.sitemaps import Sitemap

from news.models import Post
from catalog.models import Product
from catalog.urls import *

from django.core.urlresolvers import reverse


class DinamicSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, post):
        return post.published_date

    def location(self, post):
        return "/news/" + str(post.id)

class CatalogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def lastmod(self, product):
        return product.created

    def location(self, product):
        return "/" + str(product.id) + "/" + str(product.slug) + "/"

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['mainpage:PostList', 'mainpage:contact', 'mainpage:contacts',
                'mainpage:partner', 'catalog:search']

    def location(self, object):
        return reverse(object)