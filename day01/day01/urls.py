"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from jxlg01 import views
from jxlg02.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/',views.book),
    path('book_detail/',views.book_detail),
    path('books_det/<str:book_id>/<int:category_id>/',views.books_detail),
    path('',index),
    path('book/',include('jxlg01.urls'))
]
