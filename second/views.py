from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductsListSerializer, ProductsDetailSerializer
from .models import Products
from rest_framework import generics

class ProductListView(ListAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = ProductsListSerializer
    queryset = Products.objects.all()

class ProductDetailView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = ProductsDetailSerializer
    queryset = Products.objects.all()
    
class PostListView(generics.ListAPIView):
    serializer_class = ProductsDetailSerializer
    queryset = Products.objects.all()
