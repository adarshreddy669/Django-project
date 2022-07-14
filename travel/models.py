from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField(("price"))
    rating=models.IntegerField(("4-star rating"))
    days=models.IntegerField(("5-day tour"))
    offer=models.BooleanField(default=False)