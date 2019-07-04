from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import View
from apps.jxlg0102auth.models import *


# Create your views here.
class AddBookView(View):
    def post(self, request, *args, **kwargs):
        return render(request, "cms/add_book.html")

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("您当前采用的method是：%s，本视图只支持使用post请求！" % request.method)


class SuperUserLoginView(View):
    def get(self, request):
        return render(request, 'cms/login.html')

    def post(self, request):
        return redirect(reverse('add_book'))


def my_news(request):
    return render(request, 'cms/my_news.html')


# 我的收藏
def mytable(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    # username = request.front_user.username
    books = user.book_set.all()
    context = {
        'books': []
    }
    for book in books:
        time = book.update_time.strftime('%Y-%m-%d')
        booket = [book.id, book.title, time, book.author]
        context['books'].append(booket)
    return render(request, 'cms/mytable.html', context=context)


def user_info(request):
    return render(request, 'cms/user_info.html')
def logout(request):
    request.session.flush()
    return redirect(reverse('news:index'))
def book_detail(request, book_id):
    # 查询当前书籍的信息
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=book.author_id)
    # 确认是否收藏
    user_id = request.session.get('user_id')
    massage = ""
    if user_id != None:
        user = User.objects.get(pk=user_id)
        collection = book.user_book.filter(username=user.username)
        if collection:
            massage = "已收藏"
    return render(request, 'cms/book_detail.html', {"books": book, "author": author, "massage": massage})
# 增加收藏
def collection_add(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        # print(book_id)
        book = Book.objects.get(id=book_id)
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        book.user_book.add(user)
        return redirect(reverse("cms:book_detail", kwargs={'book_id': book_id}))
    else:
        raise RuntimeError("增加图书的方法必须是post")


def collection_del(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        print(book_id)
        book = Book.objects.get(id=book_id)
        # print(book.update_time)
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        print(user.username)
        book.user_book.remove(user)
        print(book.user_book)
        # print('ddd')
        return redirect(reverse('cms:my_table'))
    else:
        raise RuntimeError("删除图书的方法必须是post")


def author_detail(request):
    author_id = request.GET.get('author_id')
    ret = Author.objects.get(id=author_id)
    # 查出该作者下的所有作品
    books = ret.book_set.all()
    return render(request, 'cms/author_detail.html', {"author": ret, "books": books})


def add_article(request):
    return render(request, 'cms/add_article.html')


class AddAuthorView(View):
    def get(self, request):
        return render(request, 'cms/add_author.html')

    def post(self, request):
        true_name = request.POST.get("name")
        pen_name = request.POST.get("pen_name")
        days = request.POST.get("days")
        file = request.FILES['logo']
        if file:
            Author.objects.create(true_name=true_name, pen_name=pen_name, days=days, image=file)
            return render(request, 'cms/index.html')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("您当前采用的method是：%s，本视图只支持使用post请求！" % request.method)
