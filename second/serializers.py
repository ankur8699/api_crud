from rest_framework import serializers
from .models import Products


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'price', 'category')
        

class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'price', 'description', 'category', 'image')     