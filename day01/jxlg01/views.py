from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def book(request):
    return HttpResponse('江西理工大学')
def book_detail(request):
    book_id = request.GET['id']
    text = "您要查看的图书id是%s" % book_id
    return HttpResponse(text)
def books_detail(request,book_id,category_id):
    text = "您要查看到图书id是%s分类是%s" % (book_id,category_id)
    return HttpResponse(text)