from django.db import models
from .forms import User

# Create your models here.
class menus(models.Model):
    dishname=models.CharField(max_length=20)
    discription=models.CharField(max_length=100)
    price=models.IntegerField()
    dish_pic=models.FileField()

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(menus,on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now_add=True)

class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)  
    phone=models.CharField(max_length=20)
    address=models.TextField(max_length=1000)
    items=models.JSONField()
    total_price=models.IntegerField()
    order_status=models.CharField(max_length=20)
    amount_status=models.CharField(max_length=20)
    order_time=models.DateTimeField(auto_now=True)