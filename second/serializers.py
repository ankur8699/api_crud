from rest_framework import serializers 
from .models import Products, Details
        
class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ( 'id','ids', 'color',  'image')

class ProductsListSerializer(serializers.ModelSerializer):
    product_details=DetailsSerializer(read_only=True , many=True)
    class Meta:
        model = Products
        fields = ('id', 'title','price', 'category','product_details')   

