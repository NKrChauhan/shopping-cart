from django.urls import path
from .views.product import ProductView, ProductListView

urlpatterns = [
    path('product/<int:pk>/', ProductView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/', ProductListView.as_view()),
]
