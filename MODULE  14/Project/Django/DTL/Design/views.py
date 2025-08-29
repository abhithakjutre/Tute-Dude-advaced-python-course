from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    # return HttpResponse("<h1> Hello </h1>")
    return render(request,"home.html")


def add(request):
    value1 = int(request.POST['number 1'])
    value2 = int(request.POST['number 2'])
    res = value1 + value2
    return render(request,'result.html',{'result' : res})