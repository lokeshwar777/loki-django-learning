from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is Loki Django Learning home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is Loki Django Learning about page")

def contact(request):
    return HttpResponse("This is Loki Django Learning contact page")
    