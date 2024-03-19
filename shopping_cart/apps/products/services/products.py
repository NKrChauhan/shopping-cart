from django.forms import ValidationError
from .product_category import ProductCategoryService
from ..models import Product
from ..exceptions import ProductNotFound


class ProductService:
    def get_all_products(self):
        return Product.objects.all()
    
    def get_product_by_id(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            raise ProductNotFound(id)
        except:
            raise Exception("Could not found due to some issue")
        
    def delete_product(self, action_user, id):
        product = self.get_product_by_id(id=id)
        if product.created_by.email == action_user.email or action_user.is_superuser:
            try:
                product.delete()
                return True
            except:
                return False
        raise PermissionError

    def create(self, action_user, data):
        category_names = data.pop('category_names')
        categories = ProductCategoryService().get_or_create_categories(category_names)
        # Set the creator field
        product = Product(**data)
        product.created_by = action_user
        product.save()
        product.categories.set(categories)
        return product
    
    def update(self, action_user, instance, data):
        if instance.created_by.email == action_user.email or action_user.is_superuser:
            category_names = data.pop('category_names', [])  # Extract category words (optional)
            categories = ProductCategoryService().get_or_create_categories(category_names)
            
            print(instance, action_user, data)
            for key, value in data.items():
                setattr(instance, key, value)         

            # Update categories using categories.set() (optional)
            if categories:  # Update categories only if provided
                instance.categories.set(categories)

            instance.save()
            
            return instance
        raise PermissionError
        