from django.urls import path
from .views import *

urlpatterns = [
   path('', index, name="index"),
   path('books', view_all_books, name='all_books'),
   path('books/<int:bookid>', view_single_book, name='single_book'),
   path('books/year/<int:year>', view_book_by_year, name='view_book_year'),
   path('books/genre/<str:genre>', view_book_by_category, name='view_by_category'),
   # path('books/genre/<str:genre>/year/<int:year>', view_book_by_category_and_year, name='view_by_category_and_year'),
   path('customer/<int:customerid>', view_customer_by_book, name='customer'),
]
