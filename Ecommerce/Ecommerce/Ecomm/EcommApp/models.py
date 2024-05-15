from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator ,MinValueValidator

# Create your models here.
class CustomManager(models.Manager):
    def mobile(self):
        return self.filter(prod_category__iexact='mobile')
    def tv(self):
         return self.filter(prod_category__iexact='tv')

class Products(models.Model):
    CATEGORY = [
        ('mobile','MOBILE'),
        ('laptop','LAPTOP'),
        ('tv','TV'),
    ]
    
    
    prod_id=models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length=20)
    prod_category = models.CharField(max_length=100,choices=CATEGORY)
    prod_desc = models.CharField(max_length=255)
    prod_price = models.IntegerField()
    prod_image = models.ImageField(upload_to='Product_Images')
    products=CustomManager()
    objects= models.Manager()


    def __str__(self) -> str:
        return f"{self.prod_name}"


class CartItem(models.Model):

    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="",null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.quantity} - {self.product.prod_name}"



class Order(models.Model):
    order_id =models.CharField(max_length=100,default="0")
    product =models.ForeignKey(Products,on_delete= models.CASCADE)
    quantity =models.PositiveIntegerField(default= 1)
    date_added =models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE ,default= "" ,blank=True ,null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.product.prod_name}"   
    


class Address(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    zipcode=models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])    
    phone =models.BigIntegerField()

    def __str__(self) -> str:
        return self.address 