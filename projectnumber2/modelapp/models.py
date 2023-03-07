from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length = 10)


class Car(models.Model):
    COLOR_CHOICES = (
        ("w", "white"),
        ("b", "black"),
    )
    name = models.CharField(max_length = 10)
    color = models.CharField(max_length = 10, choices = COLOR_CHOICES)
    factory = models.ForeignKey(Factory, on_delete = models.CASCADE)
    price = models.IntegerField()

