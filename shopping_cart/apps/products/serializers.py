from rest_framework import serializers
from django.contrib.auth import get_user_model

from .services.products import ProductService
from .models.product import Product, ProductCategory
from .services.product_category import ProductCategoryService

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    categories = ProductCategorySerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'  # Include all fields (or specify specific fields)


class ProductCreateUpdateSerializer(ProductSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    category_names = serializers.ListField(child=serializers.CharField(), required=False)
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        return ProductService().create(self.context['request'].user,validated_data)

    def update(self, instance, validated_data):
        return ProductService().update(self.context['request'].user, instance, validated_data)
