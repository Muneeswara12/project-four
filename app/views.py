from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def muni(request):
    return render(request,'muni.html')


def muni1(request):
    return render(request,'muni.html')

def muni2(request):
    return HttpResponse('muni,hello')

def muni3(request):
    return HttpResponse('<h1>new new</h1><marquee>new</marquee>')