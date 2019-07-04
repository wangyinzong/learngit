from django.shortcuts import render,redirect,reverse
from .models import Article
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods,require_GET,require_POST
# Create your views here.
# @require_http_methods(['GET','POST'])
# @require_http_methods(['GET'])
@require_GET
def index(request):
    return HttpResponse('f')
# 先让用户看到文章页面，提交用户请求数据到视图函数
@require_http_methods(['GET','POST'])
def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        Article.objects.create(title=title,content=content,price=price)
        return redirect(reverse('index'))