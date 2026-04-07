from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
    CategoryDetailView,
    CategoryProductsView,
)

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:id>/', CategoryDetailView.as_view()),
    path('categories/<int:id>/products/', CategoryProductsView.as_view()),
]