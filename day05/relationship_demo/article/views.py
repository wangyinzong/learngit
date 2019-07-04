from django.shortcuts import render
from .models import Article, Category,UserExtension,Tag
from frontus.models import FrontUser
from django.http import HttpResponse
# Create your views here.
def index(request):
    category = Category(name="江西")
    category.save()
    article = Article(title="第一薇恩",content="一个打五个的薇恩怕不怕")
    article.category=category
    article.save()
    # article = Article.objects.first()
    # print(article.category.name)
    return HttpResponse("成功")

def one_to_many_view(request):
    # article = Article(title="你好", content="我是你吗的九九")
    # category = Category.objects.first()
    # author = FrontUser(name="王银宗")
    # author.save()
    # article.category = category
    # article.author = author
    # article.save()
    # category = Category.objects.first()
    # articles = category.article_set.all()
    # for article in articles:
    #     print(article)
    # category = Category.objects.first()
    # articles = category.articles.all()
    # for article in articles:
    #     print(article)
    category = Category.objects.first()
    article = Article(title="无词",content="随风潜入夜，润物细无声")
    article.author = FrontUser.objects.first()
    category.articles.add(article,bulk=False)
    return HttpResponse("一对多")
def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # extension = UserExtension(school="三抗秒")
    # extension.user=user
    # extension.save()
    extension = UserExtension.objects.first()
    print(extension.user)
    user = FrontUser.objects.first()
    extensions = user.extension
    print(extensions)

    return HttpResponse("成功了")
def many_to_many_view(request):
    # article = Article.objects.all()
    # tag = Tag(name="王大胆")
    # tag.save()
    # # article.tag_set.add(tag)
    # article.tags.add(tag)
    # tag = Tag.objects.get(pk = 2)
    # article = Article.objects.get(pk = 3)
    # tag.articles.add(article)
    article = Article.objects.get(pk = 1)
    tags = article.tags.all()
    for tag in tags:
        print(tag)
    return HttpResponse("成功了哈")