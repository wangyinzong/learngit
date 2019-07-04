from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .forms import MessageBoardForm,RegisterForm
from django.http import HttpResponse
from .models import User
from django.forms.utils import ErrorDict


class IndexView(View):
    def get(self,request,*args,**kwargs):
        if request:
            title = request.GET.get('title')
            content = request.GET.get('content')
            email = request.GET.get('email')
            reply = request.GET.get('reply')
            print("*" * 100)
            print(title)
            print(content)
            print(email)
            print(reply)
            print("*" * 100)
        form = MessageBoardForm
        return render(request,'index.html',context={"form":form})
    def post(self,request,*args,**kwargs):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print("*"*100)
            print(title)
            print(content)
            print(email)
            print(reply)
            print("*"*100)
            return HttpResponse("ok")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("fail")
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            telephone = form.cleaned_data.get("telephone")
            email = form.cleaned_data.get("email")
            User.objects.create(username=username,telephone=telephone,email=email)
            return HttpResponse("注册成功")
        else:
            print(form.get_errors())
            return HttpResponse("注册fail")

