from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    instructor = models.CharField(max_length=20)
    rating = models.IntegerField()
    price = models.FloatField()
