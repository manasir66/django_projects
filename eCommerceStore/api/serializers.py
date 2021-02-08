from rest_framework import serializers
from .models import Categories, Products

class CategoriesSerializer():

    class Meta:

        fields = '__all__'
        model = Categories

class ProductsSerializer():

    class Meta:

        fields = '__all__'
        model = Products