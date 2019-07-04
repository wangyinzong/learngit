from django.http import HttpResponse
from django.shortcuts import render
def greet(word):
    return "heelo word %s" % word
def index(request):
    return render(request,'index.html')
def add_view(request):
    context ={
        'v1':['1','2','3'],
        'v2':['4','5','6'],
    }
    return render(request,'add.html',context=context)