from django.db import models

# Create your models here.

class Categories(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Products(models.Model):

    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    imageURL = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Categories, related_name='products', on_delete=models.CASCADE)

    class Meta:

        ordering = ["-date_created"]
    

    def __str__(self):
        return f"{self.tag} {self.name}"

