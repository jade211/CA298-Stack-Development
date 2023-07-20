from django.urls import path, include
from .views import *

# import this statements
from rest_framework import routers

# create and define our router 
router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'book', BookViewSet)
router.register(r'borrow', BorrowViewSet)



urlpatterns = [
   path('', index, name="index"),
   path('books', view_all_books, name='all_books'),
   path('books/<int:bookid>', view_single_book, name='single_book'),
   path('books/year/<int:year>', view_book_by_year, name='view_book_year'),
   path('books/genre/<str:genre>', view_book_by_category, name='view_by_category'),
   path('books/genre/<str:genre>/year/<int:year>', view_book_by_category_and_year, name='view_by_category_and_year'),
   path('customer/<int:customerid>', view_customer_by_book, name='customer'),
   
   path('add', api_add, name='api_add'),
   path('subtract', api_subtract, name='api_subtract'),
   path('divide', api_divide, name='api_divide'),
   path('multiply', api_multiply, name='api_multiply'),
   path('exponential', api_exponential, name='api_exponential'),
   path('api', include(router.urls)), # add the router to our urls
]

