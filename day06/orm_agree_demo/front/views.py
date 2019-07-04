from django.shortcuts import render
from .models import Book,BookOrder,Publisher
from django.http import HttpResponse
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
from django.db import connection
# Create your views here.

def index(request):
    result = Book.objects.aggregate(avg=Avg("price"))
    # result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    print(result)
    # print(result.query) 只有filter 才可以用query查询语句
    print(connection.queries)
    return HttpResponse('成功')
def index1(request):
    result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    print(result)
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    # print(result.query) 只有filter 才可以用query查询语句
    for book in books:
        print("%s:%s"%(book.name,book.avg))
    print(connection.queries)
    return HttpResponse('成功')