from ..models import ProductCategory

class ProductCategoryService:
    def get_or_create_categories(self, categories):
        categories_objects = []
        for word in categories:
            category, created = ProductCategory.objects.get_or_create(name=word)
            categories_objects.append(category)
        return categories_objects