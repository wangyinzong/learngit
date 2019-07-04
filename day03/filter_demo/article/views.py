from django.shortcuts import render

# Create your views here.
from datetime import datetime


def index(request):
    context = {
        'mytime':datetime(year=2019,month=6,day=13,hour=9,minute=24,second=30)
    }
    return render(request,'index.html',context=context)