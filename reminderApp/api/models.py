from django.db import models

# Create your models here.

class Reminders(models.Model):

    reminder = models.CharField(max_length=100)
    completed = models.BooleanField(default=False, null=False)


    def __str__(self):
        return self.reminder


class Notes(models.Model):

    title = models.CharField(max_length=25)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    