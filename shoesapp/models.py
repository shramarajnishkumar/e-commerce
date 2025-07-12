import email
from msilib.schema import Class
from pickle import TRUE
from secrets import choice
from unicodedata import name
from django.db import models
import random as r
from myapp.models import *

pics=['logo1.jpg','logo2.png','logo3.jpg','logo4.png','logo5.png','logo6.png','logo7.png','logo8.png','logo9.png','logo10.png','logo11.png','logo12.png','logo13.png','logo14.png','logo15.png','logo16.png']
logo=r.choice(pics)

class Register(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=13)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=60)
    password=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='Profile Pic',default=logo)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=50,null=True)
    message=models.TextField(max_length=200)
    enq_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=60)
    message=models.CharField(max_length=500)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    size = models.CharField(max_length=60)
    qty = models.IntegerField()
    cart=models.ForeignKey(product,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.name  

class Order(models.Model):

    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    address=models.TextField(max_length=60)
    pay_mode = models.CharField(max_length=50,choices=[('cod','cod'),('online','online')])
    pay_id = models.CharField(max_length=30,null=True,blank=True)
    verify = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)
    pay_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.pay_at)