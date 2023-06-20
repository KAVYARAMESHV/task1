from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE,default=1)



class product(models.Model):
    productname=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    photo=models.CharField(max_length=200)
    price=models.CharField(max_length=5)
    BRAND=models.CharField(max_length=50)

class cart(models.Model):
    PRODCUT = models.ForeignKey(product,on_delete=models.CASCADE,default=1)
    USER = models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    quantity = models.CharField(max_length=10)
    date = models.DateField(max_length=10)
    total = models.CharField(max_length=50)