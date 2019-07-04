from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('后台首页')
    else:
        # login_url = reverse('front:login')
        # print("="*50)
        # print(login_url)
        # return redirect(login_url)
        current_namespace = request.resolver_match.namespace
        print(current_namespace)
        return redirect(reverse("%s:login" % current_namespace))
def login(request):
    return HttpResponse("后台登录首页")