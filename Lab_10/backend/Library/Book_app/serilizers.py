# serializers.py created inside your app folder
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ['id','name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['id','year', 'author', 'title', 'genre', 'inventory_number']


class BorrowSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Borrow
		fields = ['id', 'customer', 'books', 'due_date', 'is_returned']
