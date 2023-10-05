from django.db import models

class Vechicles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    price=models.PositiveIntegerField()


