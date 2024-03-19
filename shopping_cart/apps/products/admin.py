from django.contrib import admin
from .models.product import Product, ProductCategory


admin.site.register(Product)
admin.site.register(ProductCategory)