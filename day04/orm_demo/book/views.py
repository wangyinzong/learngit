from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.
# class Person(object):
#     username = 'ad'
#     age = 19
#     height = '151cm'
# person = Person()

def index(request):
    # book = Book(name="book数据库",author="作者1",price=22.3)
    # book.save()
    # book = Book.objects.get(pk=1)
    book = Book.objects.filter(name="book数据库").first()
    print(book)
    # book = Book.objects.get(pk=1)
    # book.delete()
    # book = Book.objects.get(pk=2)
    # book.price=100
    # book.save()
    return HttpResponse("成功")