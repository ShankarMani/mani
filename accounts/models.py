from django.db import models

# Create your models here.
class  vendor(models.Model):
    name=models.CharField(max_length=100)
    shopname=models.CharField(max_length=100)
    shopaddress=models.CharField(max_length=200)
    shopLicienceName_img=models.ImageField(upload_to='lecience',blank=True)
    latitude=models.PositiveIntegerField()
    longitude=models.PositiveIntegerField()
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    is_approved=models.BooleanField(default=False)

class customer(models.Model):
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100,default=None,blank=True,null=True)
    lastname=models.CharField(max_length=100,default=None,blank=True,null=True)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.PositiveIntegerField()
    phoneNo=models.PositiveIntegerField()
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
