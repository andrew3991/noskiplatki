from django.contrib import admin
from .models import Product, Category, Undercategory


class UndercategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name', )}

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'size']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Undercategory, UndercategoryAdmin)