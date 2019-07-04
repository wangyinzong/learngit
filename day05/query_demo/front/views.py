from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Article,Category

# Create your views here.
def index(request):
    print(type(Book.objects))
    return HttpResponse("成功")
def index1(request):
    book = Book.objects.filter(name__exact="青铜段位")
    print(book.query)
    return HttpResponse("index1")
def index2(request):
    book = Book.objects.filter(name__contains="前锋")
    print(book.query)
    return HttpResponse("index2")
def index3(request):
    articles = Article.objects.filter(id__in=[1,2,3,4])
    for article in articles:
        print(article)
    print(articles.query)
    categorys = Category.objects.filter(articles__in=[1,2,3,4])
    for category in categorys:
        print(category)
    return HttpResponse("index2")
def index4(request):
    articles = Article.objects.filter(id__gte=2)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("index4")
def index5(request):
    start_time = datetime()
    return HttpResponse("index4")