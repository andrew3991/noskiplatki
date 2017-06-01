from django import forms
from .models import Order
from django.contrib.auth.models import User

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address', 'postal_code','city']

	first_name = forms.CharField(label='ФИО',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(label='ФИО',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(label='Email адресс',widget=forms.TextInput(attrs={'class': 'form-control'}))
	address = forms.CharField(label='Адрес',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	postal_code = forms.CharField(label='Код',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	city = forms.CharField(label='Город',widget=forms.TextInput(attrs={'class': 'form-control'}))
