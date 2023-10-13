from django.db import models
from django.contrib.auth.models import User

class Vechicles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    price=models.PositiveIntegerField()


    def __str__(self):
        return (self.name)  # this fuction is used to print the book name



class Reviews(models.Model):
    vechicle=models.ForeignKey(Vechicles,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment