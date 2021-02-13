from django.shortcuts import render

# Create your views here.

#we use generic views
from rest_framework import generics

#import the serializer and models
from .serializers import CategoriesSerializer, ProductsSerializer
from .models import Categories, Products

class ListCategory(generics.ListAPIView):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer