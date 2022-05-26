from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return render(request,'shop/index.html')

def about(request) :
    return render(request,'shop/about.html')

def contact(request) :
    return HttpResponse("we are in contact")

def tracker(request) :
    return HttpResponse("We are in tracker")

def search(request) :
    return HttpResponse("we are in search")

def productView(request):
    return HttpResponse("We are in product view")

def checkOut(request) :
    return HttpResponse("We are in check out")
