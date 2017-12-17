from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime
from django.utils import timezone



SIZE_CHOICES = (
	(1, '35-38'),
	(2, '39-42'),
	(3,'43-45'),
)


class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('catalog:ProductListByCategory', args=[self.slug])

class Undercategory(models.Model):
	category = models.ForeignKey(Category, related_name='undercategory', verbose_name="Категория")
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'Подкатегория'
		verbose_name_plural = 'Подкатегории'

	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
	name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение")
	description = models.TextField(blank=True, verbose_name="Описание")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
	stock = models.PositiveIntegerField(verbose_name="На складе")
	available = models.BooleanField(default=True, verbose_name="Доступен")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	size = models.IntegerField(choices=SIZE_CHOICES, default=0,  verbose_name='Размер')
	recomendation = models.BooleanField(default=False, verbose_name="Рекомендуем")
	new = models.BooleanField(default=False, verbose_name="Новый")
	akcii = models.BooleanField(default=False, verbose_name="Акции")

	class Meta:
		ordering = ['name']
		index_together = [
			['id', 'slug']
		]
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('catalog:ProductDetail', kwargs={'id': self.id, 'slug': self.slug})

class ProductLike(models.Model):
	user = models.ForeignKey(User, verbose_name='User')
	favorites_products = models.ForeignKey(Product, verbose_name='Favorites', blank=True)


	class Meta:
		unique_together = ['user', 'favorites_products']
	def get_bookmark_count(self):
		return self.productlike_set().all().count()



class Commenter(models.Model):

	user = models.ForeignKey(User, verbose_name='User')
	product = models.ForeignKey(Product, related_name='comments', verbose_name='Product')
	path = ArrayField(models.IntegerField())
	content = models.TextField('Комментарий')
	pub_date = models.DateTimeField('Дата комментария', default=timezone.now)

	def __str__(self):
		return self.content[0:200]

	def get_offset(self):
		level = len(self.path) - 1
		if level > 5:
			level = 5
		return level

	def get_col(self):
		level = len(self.path) - 1
		if level > 5:
			level = 5
		return 12 - level