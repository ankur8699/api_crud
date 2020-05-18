from rest_framework import viewsets
from . import models
from . import serializers

class ProductsViewset(viewsets.ModelViewSet):
 queryset=models.Products.objects.all()
 serializer_class=serializers.ProductsListSerializer

class DetailsViewset(viewsets.ModelViewSet):
    queryset=models.Details.objects.all()
    serializer_class=serializers.DetailsSerializer 
