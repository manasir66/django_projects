from rest_framework import serializers
from .models import Categories, Products

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:

        fields = '__all__'
        model = Categories

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:

        fields = '__all__'
        model = Products