from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10,blank=True, null=False)
    hash = models.CharField(max_length=64,blank=True, null=False)
    def __str__(self):
        return str(self.name)

class Image(models.Model):
    image = models.ImageField(upload_to='static/',blank=True, null=True)
    path = models.CharField(max_length=30,blank=True, null=True)

class Painting(models.Model):
    user_id = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=10,blank=True, null=True)
    painting = models.ImageField(upload_to='static/',blank=True, null=True)
    path = models.CharField(max_length=30,blank=True, null=True)
    date = models.DateField(max_length=10,blank=True, null=True)