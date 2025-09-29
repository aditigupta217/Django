from django.shortcuts import render, HttpResponse

def index(request):
   # return HttpResponse("This is home page")
   return render(request,'index.html')

def about(request):
    return HttpResponse("This is about page")




