from .models import Product, Category
import django_filters


SIZE_CHOICES = (
	('',''),
	(1, '35-38'),
	(2, '39-42'),
	(3,'43-45'),
)

class ProductFilter(django_filters.FilterSet):
	category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
	price_gt = django_filters.NumberFilter(name='price', lookup_expr='gt', label='Цена больше:')
	price_lt = django_filters.NumberFilter(name='price', lookup_expr='lt',label='Цена меньше:')
	size = django_filters.ChoiceFilter(choices=SIZE_CHOICES)
	class Meta:
		model = Product
		fields = {'price', 'category', 'size'}