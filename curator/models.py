from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    hash = models.CharField(max_length=64,blank=True, null=False)


    class Meta:
        managed = False
        db_table = 'db_user'

    def __str__(self):
        return str(self.name)

class Image(models.Model):
    image = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_image'

class Painting(models.Model):
    title = models.CharField(max_length=10, blank=True, null=True)
    painting = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    user_id = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_painting' 