from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .product_category import ProductCategory

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(ProductCategory, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
        app_label = 'products'
        ordering = ['-created_at']
