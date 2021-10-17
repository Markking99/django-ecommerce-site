from django.db import models

# Create your models here.

class Farmer(models.Model):
    Jina= models.CharField(max_length=250)
    location=models.CharField(max_length=500)
    specialization=models.CharField(max_length=600)
    contact=models.CharField(max_length=500)
    logo = models.FileField(upload_to='mkulima/static', default='/logo.png')

    def __str__(self) -> str:
         return self.Jina +'_'+self.location
   
class Member(models.Model):
    Name=models.CharField(max_length=250)
    Contact=models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    
