from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='homepage'),
    path('books', view_all_books, name='all_books'),
    path('books/<int:bookid>', view_single_book, name='view_single_book'),
    path('books/year/<int:year>', view_book_by_year, name='view_book_year'),
    path('books/category/<str:category>', view_book_by_category, name='view_by_category'),
    path('books/category/<str:category>/year/<int:year>', view_book_by_category_and_year, name='view_by_category_and_year')
    
]
