from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',
        views.ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$',
        views.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='registration_disallowed'),
        url(r'^login/$',
        auth_views.login,
        {'template_name': 'registration/login.html','authentication_form':LoginForm},
        name='auth_login'),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'mainpage/mainpage.html'},
        name='auth_logout'),
    url(r'^password/change/$',
        auth_views.password_change,
        {'post_change_redirect': 'auth_password_change_done'},
        name='auth_password_change'),
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='auth_password_change_done'),
    url(r'^password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect': 'auth_password_reset_done',
         'email_template_name': 'registration/password_reset_email.txt'},
        name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'post_reset_redirect': 'auth_password_reset_complete'},
        name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='auth_password_reset_complete'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='auth_password_reset_done'),
]