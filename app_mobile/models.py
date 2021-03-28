from django.db import models
from datetime import date
# Create your models here.

class Mobile(models.Model):

    brand_name = models.CharField(max_length=20, unique=True)
    model_name = models.CharField(max_length=20)
    price = models.IntegerField(default=1000)
    specifications = models.TextField()
    image = models.ImageField(upload_to='images')
    image_1 = models.ImageField(upload_to='images')
    image_2 = models.ImageField(upload_to='images')
    image_3 = models.ImageField(upload_to='images')
    quantity = models.IntegerField()

    def __str__(self):
        return self.model_name

class Order(models.Model):
    user = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.IntegerField()
    model_name = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateField(default=date.today())
    status = models.CharField(max_length=50,default='Pending')
    def __str__(self):
        return self.model_name



class Cart(models.Model):
    user = models.CharField(max_length=20)
    mobile_id = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.mobile_id)



