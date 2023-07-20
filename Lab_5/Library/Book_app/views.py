from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse # import the jsonresponse object
from rest_framework import viewsets
from .serilizers import *


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



# assumes get parameters 
# num1 and num2
# e.g. http://127.0.0.1:8000/add?num1=5&num2=6 returns 11
def api_add(request):
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	added = num1 + num2 # calculate the added value
    # prepare a dict to return as a json response
    # we have to give the value 'added' a key we will call 'result'
	resp_dict = {'result':added}
	return JsonResponse(resp_dict) # return the dict as a json respone

def api_subtract(request):
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	subtract = num1 - num2 # calculates num1 minus num2 value
	resp_dict = {'result':subtract}
	return JsonResponse(resp_dict) # return the dict as a json respone


def api_divide(request):
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	divide = num1 / num2 # calculates num1 divided by num2 value
	resp_dict = {'result':divide}
	return JsonResponse(resp_dict) # return the dict as a json respone

def api_multiply(request):
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	multiply = num1 * num2 # calculates the multiplied value
	resp_dict = {'result':multiply}
	return JsonResponse(resp_dict) # return the dict as a json respone


def api_exponential(request):
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	exponential = num1 ** num2 # calculates num1 raised to num2
	resp_dict = {'result':exponential}
	return JsonResponse(resp_dict) # return the dict as a json respone



## viewset for customers
class CustomerViewSet(viewsets.ModelViewSet):
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()


## viewset for books
class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()


## viewset for borrows
class BorrowViewSet(viewsets.ModelViewSet):
	serializer_class = BorrowSerializer
	queryset = Borrow.objects.all()
