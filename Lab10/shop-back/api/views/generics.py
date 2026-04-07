from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer


# ─── Product Views ────────────────────────────────────────────────────────────

class ProductListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/products/  — список всех товаров
    POST /api/products/  — создать новый товар
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/products/<product_id>/ — получить товар
    PUT    /api/products/<product_id>/ — обновить товар
    DELETE /api/products/<product_id>/ — удалить товар
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'


# ─── Category Views ───────────────────────────────────────────────────────────

class CategoryListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/categories/  — список всех категорий
    POST /api/categories/  — создать категорию
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/categories/<category_id>/ — получить категорию
    PUT    /api/categories/<category_id>/ — обновить категорию
    DELETE /api/categories/<category_id>/ — удалить категорию
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'


# ─── Custom View ─────────────────────────────────────────────────────────────

class CategoryProductsAPIView(APIView):
    """
    GET /api/categories/<category_id>/products/ — все товары категории
    """

    def get(self, request, category_id):
        
        if not Category.objects.filter(pk=category_id).exists():
            return Response(
                {'error': 'Category not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        
        products = Product.objects.filter(category_id=category_id)

        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
