from django import forms
from .models import Order
from django.contrib.auth.models import User

METHOD_CHOICES = (
	(1, 'Курьерская доставка или доставка Почтой России '),
)

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email','city', 'address', 'postal_code','order_message']

	first_name = forms.CharField(label='Имя',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(label='Фамилия',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(label='Email адресс',widget=forms.TextInput(attrs={'class': 'form-control'}))
	city = forms.CharField(label='Город',widget=forms.TextInput(attrs={'class': 'form-control'}))
	address = forms.CharField(label='Адрес',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	postal_code = forms.CharField(label='Индекс',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	#method = forms.ChoiceField(label='Метод оплаты', choices=METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
	order_message = forms.CharField(label='Сообщение', required=True, widget=forms.Textarea(
				attrs={'class': 'form-control','id':'client_message', 'placeholder': 'Сообщение'}
				))
