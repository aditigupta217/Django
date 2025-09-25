from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello Everyone, this is my home page ")
     return render(request,'index.html')

def about(request):
    return HttpResponse("Hello Everyone, this is my about page ")

def contact(request):
    return HttpResponse("Hello Everyone, this is my contact page ")