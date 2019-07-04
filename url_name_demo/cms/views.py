from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    usernmae = request.GET.get('username')
    print(usernmae)
    if usernmae:
        return HttpResponse("后台首页")
    else:
        return redirect('/login/')
def login(request):
    return HttpResponse('后台登录页面')