from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Person
# Create your views here.

def index(request):
    # user = User.objects.create_user(username="wwwqqq",email="jxligong@qq.com",password="a123456")
    # user = User.objects.create_superuser(username="abcdfaff",email="jxligongdaxue@qq.com",password="a123456")
    # user.save()

    # user = User.objects.get(pk=2)
    # user.set_password('wangyinzong123')
    # user.save()
    username = 'abcdfaff'
    password = 'a123456'
    # user = User.objects.filter(username=username,password=password)
    user = authenticate(request,username=username,password=password)
    if user:
        print("登录成功",user.username)
    else:
        print("用户名或者密码错误")
    return HttpResponse("ok")
def proxys(request):
    person = Person.get_black_list()
    print(person)
    for pers in person:
        print(pers)
    return HttpResponse('cuccess')
def one_view(request):
    user = User.objects.create_user(username="hello",email="222222@qq.com",password="123456")
    user.extension.telephone = '1388888888'
    user.save()
    return HttpResponse("haodongi")
