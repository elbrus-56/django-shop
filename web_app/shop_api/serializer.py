from rest_framework import serializers

from shop.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('title', 'description', 'price', 'category')
