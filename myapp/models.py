from datetime import date
from ntpath import join
from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=25,null=True)
    address = models.TextField(null= True)
    mobile = models.CharField(max_length=50,null=True)
    doj = models.DateField(null=True)
    pic = models.ImageField(upload_to='Profile Pic',default='avtar.png')

    def __str__(self):
        return self.email
          
class Category(models.Model):
    choices = (('Man','Man'),('Woman','Woman'),('Kid','Kid'))   
    category = models.CharField(max_length=50,choices=choices)

    def __str__(self):
        return self.category


class product(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description= models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='product pic',default='avtar.png')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
