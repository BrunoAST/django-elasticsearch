from rest_framework import viewsets

from demo.models.category import Category
from demo.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    