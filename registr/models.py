# from django.conf import settings
# from django.db import models

# from django.contrib.sessions.models import Session
# from django.contrib.auth.signals import user_logged_in



# class UserSession(models.Model):
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL)
# 	session = models.ForeignKey(Session)
# 	username = models.CharField(max_length=30)

# def user_logged_in_handler(sender, request, user, **kwargs):
#     record = UserSession.objects.get_or_create(
#         user = user,
#         username = request.user.username,
#         session_id = request.session.session_key
#     )


# user_logged_in.connect(user_logged_in_handler)

