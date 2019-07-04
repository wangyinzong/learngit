from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view_405(request):
    return render(request,'errors/405.html',status=405)
def view_403(request):
    return render(request,'errors/403.html',status=403)