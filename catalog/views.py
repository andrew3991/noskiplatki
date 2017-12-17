from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Category, Product, ProductLike, Commenter
from cart.forms import CartAddProductForm
from .forms import CommentForm
from .filters import ProductFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from catalog.templatetags import query_update
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import json
from django.template.context_processors import csrf
from django.views.decorators.http import require_http_methods

from django.contrib import auth



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

	paginator = Paginator(product_filter.qs, 9)
	page = request.GET.get('page', 1)
	try:
		product_list = paginator.page(page)
	except PageNotAnInteger:
		product_list = paginator.page(1)
	except EmptyPage:
		product_list = paginator.page(paginator.num_pages)


	return render(request, 'catalog/1.html',  {'f':product_filter, 'filter': product_list, 'wishlist':wishlist})



# def ProductDetail(request, id, slug):
# 	product = get_object_or_404(Product, id=id, slug=slug, available=True)
# 	comments =  Commenter.objects.filter(product_id=product.id).order_by('path') 
# 	cart_product_form = CartAddProductForm()
# 	comment_form = CommentForm()
# 	return render(request, 'catalog/detail.html', {'product':product, 'comments':comments,
# 	 						'cart_product_form': cart_product_form,
# 	 						'comment_form':comment_form })	




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
class EProductView(View):
	template_name = 'catalog/detail.html'
	comment_form = CommentForm
	cart_product_form = CartAddProductForm
	def get(self, request, *args, **kwargs):
		product = get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])
		context = {}
		context.update(csrf(request))
		user = auth.get_user(request)
        # Помещаем в контекст все комментарии, которые относятся к статье
        # попутно сортируя их по пути, ID автоинкрементируемые, поэтому
        # проблем с иерархией комментариев не должно возникать
		context['user'] = user
		context['product'] = product
		context['comments'] = product.comments.all().order_by('path')
		context['next'] = product.get_absolute_url()
        # Будем добавлять форму только в том случае, если пользователь авторизован
		context['cart_product_form'] = self.cart_product_form
		if user.is_authenticated:
			context['comment_form'] = self.comment_form
 
		return render_to_response(template_name=self.template_name, context=context)




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
		return HttpResponse(status=404)



def add_comment(request, id):
 
	form = CommentForm(request.POST)
	product = get_object_or_404(Product, id=id)
 
	if form.is_valid():
		comment = Commenter()
		comment.path = []
		comment.product = product
		comment.user = auth.get_user(request)
		comment.content = form.cleaned_data['comment_area']
		comment.save()

		try:
			comment.path.extend(Commenter.objects.get(id=form.cleaned_data['parent_comment']).path)
			comment.path.append(comment.id)
		except ObjectDoesNotExist:
			comment.path.append(comment.id)
 
		comment.save()
 
	return redirect('/5/akciii')