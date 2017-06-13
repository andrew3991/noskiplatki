from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from catalog.models import Product, ProductLike


class ESearchView(View):
	template_name = 'search/search.html'

	def get(self, request, *args, **kwargs):
		context = {}
		wishlist = []
		wishlists = ProductLike.objects.filter(user=request.user.id)
		for e in wishlists:
			wishlist.append(e.favorites_products_id)
		context['wishlist'] = wishlist
		product = request.GET.get('q')
		if product is not None:
			search_products = Product.objects.filter(Q(name__icontains=product))

	# формируем строку URL, которая будет содержать последний запрос
	# Это важно для корректной работы пагинации
			context['last_question'] = '?q=%s' % product
			current_page = Paginator(search_products, 10)

			page = request.GET.get('page')
			try:
			    context['article_lists'] = current_page.page(page)
			except PageNotAnInteger:
			    context['article_lists'] = current_page.page(1)
			except EmptyPage:
			    context['article_lists'] = current_page.page(current_page.num_pages)

		return render_to_response(template_name=self.template_name, context=context)