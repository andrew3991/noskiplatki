from django import forms
from .models import Client
from django.utils.translation import ugettext
from django.forms.extras.widgets import SelectDateWidget

class ClientForm(forms.ModelForm):

	class Meta:
		model = Client
		fields = ['name','email', 'number_phone', 'client_message']
		widgets = {
			'name':forms.TextInput(
				attrs={'class': 'form-control','id':'name', 'required': True, 'placeholder': 'ФИО'}
				),
			'email':forms.TextInput(
				attrs={'class': 'form-control','id':'email', 'required': True, 'placeholder': 'email'}
				),
			'number_phone':forms.TextInput(
				attrs={'class': 'form-control','id':'number_phone', 'required': True, 'placeholder': 'Телефон'}
				),
			'client_message':forms.Textarea(
				attrs={'class': 'form-control','id':'client_message', 'required': False, 'placeholder': 'Сообщение'}
				),
		}