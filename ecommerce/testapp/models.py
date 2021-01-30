from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    discounted_price=models.IntegerField()
    category=models.CharField(max_length=50)
    description=models.TextField()
    image=models.CharField(max_length=100)


class Confirmation(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    alternate_number=models.IntegerField()
    email_id=models.CharField(max_length=70)
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=70)
    pincode=models.IntegerField()
