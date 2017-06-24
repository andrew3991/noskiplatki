"""
Forms and validation code for user registration.

Note that all of these forms assume your user model is similar in
structure to Django's default User class. If your user model is
significantly different, you may need to write your own form class;
see the documentation for notes on custom user models with
django-registration.

 


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username','placeholder':'Email address'}))

    password = forms.CharField(label="Password", max_length=30, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Password'}))



from django import forms
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import PasswordInput, TextInput
"""
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm,RegistrationFormUniqueEmail
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


import uuid

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'class': 'required'}




class MyCustomUserForm(RegistrationFormUniqueEmail):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'name': 'username','placeholder':'Логин'}))

    email = forms.EmailField(help_text=None, required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Email'}))
    
    password1 = forms.CharField(
        help_text=None,widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Пароль'})
    )

    password2 = forms.CharField(
        help_text=None,widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Повторите пароль'})
    )
   
    def clean_password(self):
        if self.data['password1'] != self.data['password2']:
            raise forms.ValidationError('Passwords are not the same')
        return self.data['password1']

class EmailOnlyAuthenticationForm(AuthenticationForm):
    """
    Subclass of django.contrib.auth.AuthenticationForm that accepts
    emails for usernames
    """
    username = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)), 
                                label=_("E-mail / Username"))

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'name': 'username','placeholder':'Email или Логин'}))

    password = forms.CharField(label="Password", max_length=30, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Пароль'}))
