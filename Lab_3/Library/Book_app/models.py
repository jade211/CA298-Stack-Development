from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.TextField()
    title = models.TextField()
    genre = models.CharField(max_length=30, default='fantasy')
    inventory_number = models.IntegerField()


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

class Borrow(models.Model):
    id = models.AutoField(primary_key=True)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    is_returned = models.BooleanField(default=False)
