import json
import random
from uuid import UUID

import requests
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate

from apps.jxlg0102auth.models import *
import sys


# Create your views here.
def index(request):
    # for i in range(1,76):
    #     month_ticket = i*random.randint(100, 300)
    #     commend = i*random.randint(100, 300)
    #     count = i*random.randint(100, 300)
    #     days = i*random.randint(10,30)
    #     author = Author.objects.create(true_name='作者%s'%i,pen_name='王%sX'%i,days=days)
    #     book = Book.objects.create(title='书名字%s'%i,content='简介%s'%i,category='分类%s'%i,count=count,author=author,image='url',month_ticket=month_ticket,commend=commend,words="%s万"%i)
    # for i in range(1,76):
    #     books = Book.objects.filter(id=i)
    #     for book in books:
    #         if i%6 == 0:
    #             book.category = 'xuanhuan'
    #         if i%6 == 1:
    #             book.category = 'doushi'
    #         if i%6 == 2:
    #             book.category = 'kehuan'
    #         if i%6 == 3:
    #             book.category = 'lishi'
    #         if i%6 == 4:
    #             book.category = 'youxi'
    #         if i%6 == 5:
    #             book.category = 'xianxia'
    #         book.save()

    # print('ok')
    # books = Book.objects.filter(id__lt=30)[0:15]
    # for book in books:
    #     print(book.title)
    # ii = 10
    # jj = 99
    # for i in range(10,88):
    #     ii = ii+1
    #     jj = jj-1
    # user = User.objects.create_user(telephone='18825437784', username='张三大', password='123456', email='112323@qq.com')
    # 添加uer和book关系
    # user = User.objects.filter(username='王某2')
    # for users in user:
    #     for i in range(1,21):
    #         id = random.randint(1,54)
    #         books = Book.objects.filter(id=id)
    #         for book in books:
    #             book.user_book.add(users.uid)
    #     print(users.username)
    # booket = Book.objects.get(title="飞升传")
    # booket.user_book.add(user.uid)
    # print(request.front)
    # request.session.flush()
    # for i in range(1,75):
    #     print(i)
    #     ur = random.randint(0,140)
    #     book = Book.objects.get(pk=i)
    #     book.image = 'book_images/img%s.jpg'% ur
    #     book.save()
    # print('ok')
    return render(request, 'news/index.html')


def LoginRegister(request):
    return render(request, 'news/login_register.html')
def sendCode(request):
    telephone = request.POST.get('telephone')
    # print(telephone)
    # url = 'http://v.juhe.cn/sms/send'
    # params = {
    #     "mobile": telephone,  # 手机号  必须传
    #     "tpl_id": "135629",  # 模板的id
    #     "tpl_value": "#code#=" + '888889',
    #     "key": "",
    # }
    # response = requests.get(url, params=params)
    # result = response.json()
    code = []
    for i in range(1,4):
        code.append(random.randint(0,9))
    # code = '3568'
    request.session['telephone']=code
    if code != 0:
        print('ok')
        return HttpResponse("SUCCESS")
    else:
        print('no')
        return HttpResponse("FAIL")
def login(request):
    telephone = request.POST.get('telephone')
    password = request.POST.get('password')
    user_auth = authenticate(telephone=telephone, password=password)
    if user_auth is not None:
        # sys.setrecursionlimit(4000)
        user = User.objects.get(telephone=telephone)
        request.session['user_id'] = user.uid
        request.session.set_expiry(0)
        print('ok')
        return HttpResponse('SUCCESS')
    else:
        print('no')
        return HttpResponse('FAIL')

def register(request):
    telephone = request.POST.get('telephone')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    code_cms = request.session.get('cose')
    code_news = request.POST.get('dode')
    user = User.objects.filter(telephone=telephone).first()
    if user:
        return HttpResponse("telephone_repeat")
    if code_cms == code_news:
        user = User.objects.create_user(telephone=telephone,username=username,password=password,email=email)
        return HttpResponse("SUCCESS")
    else:
        return HttpResponse("CODENOFOUND")


def ranking(request):
    context = {
        'fengyunbang': [],
        'rexiaobang': [],
        'fensibang': [],
        'tuijianbang': [],
        'xinshubang': [],
    }
    # 查询数据库 根据division查询 所有数据
    for name in ['fengyunbang', 'rexiaobang', 'fensibang', 'tuijianbang', 'xinshubang']:
        if name == 'fengyunbang':
            books = Book.objects.order_by('-month_ticket')[0:15]
        elif name == 'rexiaobang':
            books = Book.objects.order_by('-count')[0:15]
        elif name == 'tuijianbang':
            books = Book.objects.order_by('-commend')[0:15]
        elif name == 'xinshubang':
            books = Book.objects.order_by('-update_time')[0:15]
        else:
            books = Book.objects.annotate(cout=Count('user_book')).order_by('-cout')[0:15]
        for bok in books:
            time = bok.update_time.strftime('%Y-%m-%d')
            book = [bok.title, bok.author, bok.category, bok.image, bok.count, bok.month_ticket, bok.commend,
                    bok.content, time,bok.id]
            context[name].append(book)
    return render(request, 'news/ranking.html', context=context)


def category(request):
    division = request.GET.get('name')
    context = {
        'category': division,
        'books_all': []
    }
    boks = Book.objects.filter(category=division)[1:36]
    i = 0
    books = []
    for bok in boks:
        i = i + 1
        boook = [bok.title, bok.content, bok.author.pen_name, bok.image, bok.count]
        if i % 3 != 0:
            books.append(boook)
        else:
            books.append(boook)
            context['books_all'].append(books)
            books = []
    return render(request, 'news/category.html', context=context)
