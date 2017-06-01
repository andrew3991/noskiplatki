from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class PostCategory(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)


	class Meta:
		ordering = ['name']
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(PostCategory, related_name='posts', verbose_name="Категория")
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True, verbose_name="Изображение")
	
	class Meta:
		ordering = ['created_date']
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('news:PostNewsDetail', args=[self.id])