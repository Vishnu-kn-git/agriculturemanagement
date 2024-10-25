from django.db import models
class Submit(models.Model):
    product=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.CharField(max_length=20,null=True,blank=True)
class feedback(models.Model):
    userid=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
class complaint(models.Model):
    userid=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    reply=models.CharField(max_length=255,null=True,blank=True) 
class policy(models.Model):
    policyname=models.CharField(max_length=255,null=True,blank=True)
    date=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True) 
class farmer(models.Model):
    farmername=models.CharField(max_length=255,null=True,blank=True)
    email=models.CharField(max_length=255,null=True,blank=True)
    contactnumber=models.CharField(max_length=255,null=True,blank=True) 
class business(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    companyname=models.CharField(max_length=255,null=True,blank=True)
    email=models.CharField(max_length=255,null=True,blank=True)
    number=models.CharField(max_length=255,null=True,blank=True)
    password=models.CharField(max_length=255,null=True,blank=True)