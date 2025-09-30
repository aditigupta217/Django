from django.shortcuts import render, HttpResponse

def index(request):
   # return HttpResponse("This is home page")
   context = {
       "variable" : "Thiss is aditis site",
       "variable1" : "ufff aditiii"
   }
   return render(request,'index.html',context)

def about(request):
    #return HttpResponse("This is about page")
    return render(request,'about.html')

def servies(request):
   # return HttpResponse("This is services page")
   return render(request,'servies.html')

def contact(request):
    #return HttpResponse("This is contact page")
    return render(request,'contact.html')

def home(request):
    #return HttpResponse("This is home page")
    return render(request,'index.html')