from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    my_list = Book.objects.all()
    return render(request, 'index.html', {'example_variable':100, 'mylist':my_list })


def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books': all_books})


def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    books = Book.objects.get(id=bookid)
    borrow = Borrow.objects.filter(books=books)
    return render(request, 'single_book.html', {'book':single_book, 'borrowing':borrow})

def view_book_by_year(request, year):
    books_by_year = Book.objects.filter(year=year)
    return render(request, 'all_books.html', {'books': books_by_year})


def view_book_by_category(request, genre):
    by_category = Book.objects.filter(genre=genre)
    return render(request, 'all_books.html', {'books': by_category})


def view_book_by_category_and_year(request, genre, year):
    books_by_category_and_year = Book.objects.filter(genre=genre, year=year)
    return render(request, 'all_books.html', {'books': books_by_category_and_year})


def view_customer_by_book(request, customerid):
    single_customer = get_object_or_404(Customer, id=customerid)
    customer = Customer.objects.get(id=customerid)
    current = Borrow.objects.filter(is_returned=False, customer=customer)
    previous = Borrow.objects.filter(is_returned=True, customer=customer)
    return render(request, 'customer.html', {'customer':single_customer, 'current': current, 'previous': previous})
