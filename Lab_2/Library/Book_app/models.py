from django.db import models

# Create your models here.

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.TextField()
    synopsis = models.TextField()
    category = models.TextField(default='fantasy')
    