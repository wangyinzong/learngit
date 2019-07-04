from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def index(request):
    #http://127.0.0.1:8000?username=xxx
    username = request.GET.get('username')
    if username:
        return HttpResponse("前台首页")
    else:
        # return redirect('/login/') #这个是写死的状态 如果一旦换成sigin 那么都得进行修改
        # print(reverse('front:signin'))
        # return redirect(reverse('signin'))
        return redirect(reverse('front:signin'))
def login(request):
    return HttpResponse("前台登陆首页")