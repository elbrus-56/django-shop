from django.shortcuts import render
from rest_framework import generics
from shop.models import Products
from shop_api.serializer import ProductsSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
