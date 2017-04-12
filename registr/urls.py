from django.conf.urls import url,include
from . import views


urlpatterns = [
	url(r'^accounts/', include('registration.backends.hmac.urls')),
]
