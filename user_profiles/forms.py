from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['phone']

	phone = forms.CharField(label='Телефон',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пример: +7(911)4585525'}))

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name', 'email']
		
	first_name = forms.CharField(label='ФИО',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(label='ФИО',  required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(label='Email адресс',widget=forms.TextInput(attrs={'class': 'form-control'}))