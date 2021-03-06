from rest_framework import serializers

from .models import Item, Photo, Product


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description',
                  'nutrition', 'effect')


class ProductPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'image')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'product', 'price', 'description',
                  'unit', 'stock')
