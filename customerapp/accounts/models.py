from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200,default='')    
    
    def __str__(self):
        return self.name


class Products(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )
    name = models.CharField(max_length=2000,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200,default='')    
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=101,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    
    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('out of delivery','out of delivery'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    products = models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    Status =  models.CharField(max_length=101,null=True,choices=STATUS)

    def __str__(self):
        return self.products.name