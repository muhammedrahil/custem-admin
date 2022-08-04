from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=250,default='')
    price=models.FloatField()
    count=models.IntegerField()
    description=models.CharField(max_length=250,default='')
    image=models.ImageField(upload_to='upload_image')

    def __str__(self):
        return self.name