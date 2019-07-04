from django.urls import path
from . import views
app_name = 'news'
urlpatterns = [
    path('',views.index,name='index'),
    path('login_register/',views.LoginRegister,name='loginregister'),
    path('login/',views.login,name='login'),
    path('regiter/',views.register,name='register'),
    path('sendCode/',views.sendCode,name='sendCode'),
    path('category/',views.category,name='category'),
    path('ranking/',views.ranking,name='ranking'),
]