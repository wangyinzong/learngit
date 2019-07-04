from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    response = HttpResponse('index')
    expires = datetime(year=2019, month=6, day=22, hour=20, minute=30, second=40)
    expires = make_aware(expires)
    response.set_cookie('user_id', 'yinzong', expires=expires, max_age=180, path='/cms/')
    return response


def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('user_id')
    return response


def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)


def my_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

from datetime import timedelta
def session_view(request):
    # expires = datetime(year=2019, month=6, day=22, hour=20, minute=30, second=40)
    # request.session.set_expiry(expires)
    # expiry = timedelta(days=2)
    # request.session.set_expiry(None)
    request.session['username'] = 'wangyinzong'
    username = request.session.get('username')
    request.session.clear_expired() # 清空过期session
    request.session.set_expiry(-1)
    print(username)
    # request.session.flush()
    # print(username)
    return HttpResponse("session view")
def get_session(request):
    pass
