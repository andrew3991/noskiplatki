from django.db import models
from catalog.models import Product
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


METHOD_CHOICES = (
	(1, 'Курьерская доставка или доставка Почтой России '),
)


class CommonInfo(models.Model):
	first_name = models.CharField(verbose_name='Имя', max_length=50,blank=True)
	last_name = models.CharField(verbose_name='Фамилия', max_length=50,blank=True)
	email = models.EmailField(verbose_name='Email', blank=True)
	address =  models.CharField(verbose_name='Адрес', max_length=250, blank=True)
	postal_code = models.CharField(verbose_name='Почтовый код', max_length=20,blank=True)
	city = models.CharField(verbose_name='Город', max_length=100,blank=True)
	

	class Meta:
		abstract = True

class Order(CommonInfo):
	user = models.ForeignKey(User, related_name='order_auth_user',blank=True,null=True )
	method = models.CharField( max_length=250, choices=METHOD_CHOICES, default='',  verbose_name='Метод')
	created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
	paid = models.BooleanField(verbose_name='Оплачен', default=False)
	order_message = models.TextField(blank=True)
	
	class Meta:
		ordering = ('created', )
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Заказ: {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

	def get_absolute_url(self):
		return reverse('user_profiles:show_order_history_detail', args=[self.id])



class OrderItem(models.Model):
	user = models.ForeignKey(User, related_name='order_auth_user_item',blank=True,null=True )
	order = models.ForeignKey(Order, related_name='items',blank=True,null=True)
	product = models.ForeignKey(Product, related_name='order_items')
	price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity