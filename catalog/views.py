from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductLike
from cart.forms import CartAddProductForm
from .filters import ProductFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from catalog.templatetags import query_update
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import json

from django.contrib import auth
from django.views import View


def ProductList(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, 'catalog/list.html', {
		'category':category,
		'categories':categories,
		'products':products
	})


def search(request):
	wishlist = []
	wishlists = ProductLike.objects.filter(user=request.user.id)
	for e in wishlists:
		wishlist.append(e.favorites_products_id)
	product_list = Product.objects.all()
	product_filter = ProductFilter(request.GET, queryset=product_list)

	paginator = Paginator(product_filter, 9)
	page = request.GET.get('page')
	try:
		product_list = paginator.page(page)
	except PageNotAnInteger:
		product_list = paginator.page(1)
	except EmptyPage:
		product_list = paginator.page(paginator.num_pages)


	return render(request, 'catalog/1.html',  {'f':product_filter, 'filter': product_list, 'wishlist':wishlist})




def ProductDetail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	return render(request, 'catalog/detail.html', {'product':product, 'cart_product_form': cart_product_form})	



# @login_required
# def like_product(request, id, slug):
# 	product = Product.objects.get(pk=id)
# 	user = request.user
# 	likes = 0
# 	if request.method == 'POST':
# 		if request.is_ajax():
# 			pk = request.POST.get('id')
# 			slug = request.POST.get('slug')
# 			if product:
# 				likes = product.likes + 1
# 				product.likes = likes
# 				product.save()
			
# 		return HttpResponse(likes)


@login_required
def like_product(request, id, slug):
	product = Product.objects.get(pk=id)
	wishlist = ProductLike.objects.filter(user=request.user.id)
	user = request.user
	if request.method == 'POST':
		if request.is_ajax():
			if ProductLike.objects.filter(user=user, favorites_products=product).exists():
				ProductLike.objects.filter(user=user, favorites_products=product).delete()
				status = 'deleted'

			else:
				b = ProductLike(user=user, favorites_products=product)
				b.save()
				status = 'added'

			response = {'status': status}

			return JsonResponse(response)
		return HttpResponse(status=405)