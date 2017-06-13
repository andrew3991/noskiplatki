from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views
from .forms import MyCustomUserForm, LoginForm
from registration.backends.hmac.views import RegistrationView
from .forms import EmailOnlyAuthenticationForm

urlpatterns = [
    url(r'^register/$',RegistrationView.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register',
    ),
    url(r'^login/$', auth_views.login,
        {'template_name': 'registration/login.html',
        'authentication_form': LoginForm, },
        name='auth_login'),
    url(r'^password/reset/$', auth_views.password_reset,
        {'post_reset_redirect': '/password/reset/done/'},
        name = "password_reset"),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done, name="password_reset_done"),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm, {'post_reset_redirect': '/password/done/'},
        name="password_reset_confirm"),
    url(r'^password/done/$',
        auth_views.password_reset_complete, name="password_reset_complete"),



    # url(r'^password/reset/$', auth_views.password_reset,
    #     {'template_name': 'registration/password_reset_form.html', },
    #     name='auth_password_reset'),

    # url(r'^password/reset/$', auth_views.password_reset,
    #     {'template_name': 'registration/password_reset_form.html', },
    #     name='auth_password_reset'),
    # url(r'^password/reset/$', auth_views.password_reset,
    #     {'template_name': 'registration/password_reset_form.html', },
    #     name='auth_password_reset'),
    # url(r'^password/reset/$', auth_views.password_reset,
    #     {'template_name': 'registration/password_reset_form.html', },
    #     name='auth_password_reset'),
    url(r'^', include('registration.backends.hmac.urls')),
]