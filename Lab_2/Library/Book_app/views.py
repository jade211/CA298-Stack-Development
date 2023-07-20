from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    my_list = Books.objects.all()
    return render(request, 'homepage.html', {'example_variable':100, 'mylist':my_list })


def view_all_books(request):
    all_books = Books.objects.all()
    return render(request, 'all_books.html', {'books': all_books})


def view_single_book(request, bookid):
   single_book = get_object_or_404(Books, id=bookid)
   return render(request, 'single_book.html', {'book':single_book})


def view_book_by_year(request, year):
    books_by_year = Books.objects.filter(year=year)
    return render(request, 'all_books.html', {'books': books_by_year})


def view_book_by_category(request, category):
    by_category = Books.objects.filter(category=category)
    return render(request, 'all_books.html', {'books': by_category})


def view_book_by_category_and_year(request, category, year):
    books_by_category_and_year = Books.objects.filter(category=category, year=year)
    return render(request, 'all_books.html', {'books': books_by_category_and_year})
