from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators import csrf
from django.contrib.auth.models import User
from .forms import UserProfileForm, UserForm
from catalog.models import ProductLike, Product
from orders.models import Order, OrderItem


def show_profile(request):
	args = {'user':request.user}
	return render (request, 'user_profiles/show_profile.html', args)

def show_profile_about(request):
	args = {'user':request.user}
	return render (request, 'user_profiles/about.html', args)

def show_profile_favorites(request):
	products = Product.objects.all()
	favorite_products = ProductLike.objects.filter(user_id=request.user.id)
	args = {'user':request.user, 'favorites_products':favorite_products, 'product':products}
	return render (request, 'user_profiles/favorite_goods.html', args)

def edite_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.userprofile)
		formset = UserForm(request.POST, instance=request.user)
		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()
			return render(request, 'user_profiles/about.html')

	else:
		user = request.user
		profile = user.userprofile
		form = UserProfileForm(instance=profile)
		formset = UserForm(instance=user)

		args = {}

		args['form']=form
		args['formset']=formset

		return render(request, 'user_profiles/profile.html', args)



def remove_like_product(request, product_id):
	user = request.user
	product = get_object_or_404(ProductLike, favorites_products_id=product_id, user_id=user)
	ProductLike.delete(product)

	return redirect('user_profiles:show_profile_favorites')

def show_order_history(request):
	user = request.user
	orders = Order.objects.filter(user_id=user.id)
	orderitems = OrderItem.objects.filter(user_id=user.id)
	args = {'orders':orders, 'orderitems':orderitems}
	return render(request, 'user_profiles/order_history.html', args)


def show_order_history_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	orderitems = OrderItem.objects.filter(order_id=order_id)
	args = {'order':order, 'orderitems':orderitems}
	return render(request, 'user_profiles/order_history_detail.html', args)