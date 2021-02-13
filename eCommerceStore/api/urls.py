from django.urls import path, include
from . import views


urlpatterns = [
    path("categories", views.ListCategory.as_view(), name="list-category")
]

