from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userAccount(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  
  def __str__(self):
    return self.user.username

class menuData(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  count = models.IntegerField()
  soldout = models.BooleanField()

class ticketData(models.Model):
  menu_id = models.IntegerField()
  barcode = models.CharField(max_length=15, unique=True)
  available = models.BooleanField()
  used = models.BooleanField()

class orderData(models.Model):
  order_time = models.DateTimeField()
  table_id = models.IntegerField()
  menu_id = models.IntegerField()
  count = models.IntegerField()
  provide = models.BooleanField()
  checkout = models.BooleanField()
  next = models.BooleanField()

class tableData(models.Model):
  name = models.CharField(max_length=50)
  use = models.BooleanField()
  message = models.CharField(max_length=500)
  ticket_price = models.IntegerField()
  discount = models.IntegerField()

class forWorkerData(models.Model):
  message = models.CharField(max_length=500)
  priority = models.CharField(max_length=10)