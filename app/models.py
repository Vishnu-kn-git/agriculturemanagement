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
