from django.shortcuts import render
from catalog.models import  Product, ProductLike
from noskiplatki import settings
from .forms import ClientForm
from .models import Client
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse


def post_list(request):
	form=ClientForm()
	products = Product.objects.filter(available=True)

	wishlist = []
	wishlists = ProductLike.objects.filter(user=request.user.id)
	for e in wishlists:
		wishlist.append(e.favorites_products_id)
	return render(request, 'mainpage/mainpage.html', {'wishlist':wishlist, 'products':products,'form':form})

def contact(request):
	if request.method == 'POST':
		if request.is_ajax():			
			name = request.POST.get('name')
			email = request.POST.get('email')
			number_phone = request.POST.get('number_phone')
			client_message = request.POST.get('client_message')
			
			response_data = {}

			client = Client(name=name, email=email, number_phone=number_phone,
							 client_message=client_message)
			client.save()

			subject = 'ЯРМАРКА'
			message = "Имя: %s \n" \
						"E-mail: %s \n" \
						"Phone: %s \n" \
						"Message: %s \n" % \
						(name, email, number_phone, client_message)
			from_email = settings.EMAIL_HOST_USER
			to_list = [settings.EMAIL_HOST_USER]

			send_mail(subject, message, from_email, to_list, fail_silently=False)

			

			response_data['name'] = client.name
			response_data['email'] = client.email
			response_data['number_phone'] = client.number_phone
			response_data['client_message'] = client.client_message

			return JsonResponse(response_data)


def partner(request):
	return render(request, 'mainpage/partner.html', {})
def contacts(request):
	return render(request, 'mainpage/contacts.html', {})