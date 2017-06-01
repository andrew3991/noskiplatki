from django.shortcuts import render
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

def OrderCreate(request):
	if request.user.is_authenticated():
		cart = Cart(request)
		# BookFormSet = inlineformset_factory(User, OrderAuthUser, fields=('city','address', 'postal_code'))
		# author = User.objects.get(id=request.user.id)
		# formset = BookFormSet(instance=author)
		user = User.objects.get(id=request.user.id)
		if request.method == 'POST':
			form = OrderCreateForm(request.POST)
			form.instance.user = User.objects.get(id=request.user.id)
			if form.is_valid():

				order = form.save()
				for item in cart:
					OrderItem.objects.create(order=order, product=item['product'],
												price=item['price'],
												quantity=item['quantity'], user_id=request.user.id)
				cart.clear()
				

				OrderCreated.delay(order.id)
				request.session['order_id'] = order.id
				
				return render(request, 'order/created.html', {'order': order})

		form = OrderCreateForm(instance=user)
		return render(request, 'order/create.html', {'cart': cart,'form': form})

	else:
		cart = Cart(request)
		if request.method == 'POST':
			form = OrderCreateForm(request.POST)
			if form.is_valid():
				order = form.save()
				for item in cart:
					OrderItem.objects.create(order=order, product=item['product'],
												price=item['price'],
												quantity=item['quantity'])
				cart.clear()
				

				OrderCreated.delay(order.id)
				request.session['order_id'] = order.id
				
				return render(request, 'order/created.html', {'order': order})


		form = OrderCreateForm()
		return render(request, 'order/create.html', {'cart': cart,'form': form})


	