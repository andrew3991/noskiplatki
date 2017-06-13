from .models import Product, Category
import django_filters
from django import forms

SIZE_CHOICES = (
	('',''),
	(1, '35-38'),
	(2, '39-42'),
	(3,'43-45'),
)

NEW_CHOICES = (
	('', 'Выберите'),
	(True, 'Да'),
	(False,'Нет'),
)
AKCII_CHOICES = (
	('', 'Выберите'),
	(True, 'Да'),
	(False,'Нет'),
)

class ProductFilter(django_filters.FilterSet):
	category = django_filters.ModelChoiceFilter(label='Категория', queryset=Category.objects.all())
	price_gt = django_filters.NumberFilter(name='price', lookup_expr='gt', label='Цена больше:')
	price_lt = django_filters.NumberFilter(name='price', lookup_expr='lt',label='Цена меньше:')
	size = django_filters.ChoiceFilter(label='Размер', choices=SIZE_CHOICES)
	new = django_filters.ChoiceFilter(label='Новинки',choices=NEW_CHOICES)
	akcii = django_filters.ChoiceFilter(label='Акции', choices=AKCII_CHOICES)
	
	class Meta:
		model = Product
		fields = {'price', 'category', 'size', 'new', 'akcii'}