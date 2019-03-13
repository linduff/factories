from django.db import models

# Create your models here.

class Factory(models.Model):
    name = models.CharField(max_length = 30)
    minimum = models.IntegerField()
    maximum = models.IntegerField()


class Child(models.Model):
    factory_id = models.ForeignKey(Factory, on_delete=models.CASCADE)
    value = models.IntegerField()

