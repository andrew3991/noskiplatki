from django.db import models
from django.conf import settings

class Client(models.Model):
	name = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	number_phone = models.CharField(max_length=15, unique=True)
	client_message = models.TextField(blank=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.number_phone