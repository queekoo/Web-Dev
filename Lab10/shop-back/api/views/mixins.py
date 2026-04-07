from rest_framework import mixins, generics
from api.models import Product
from api.serializers import ProductSerializer


class ProductListAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    GET  /api/products/  — список всех товаров
    POST /api/products/  — создать новый товар
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """
    GET    /api/products/<product_id>/ — получить товар
    PUT    /api/products/<product_id>/ — обновить товар
    DELETE /api/products/<product_id>/ — удалить товар
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

  
    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
