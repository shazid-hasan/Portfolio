from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def inner(request):
    return render(request,'inner-page.html')

def port(request):
    return render(request,'portfolio-details.html')


# Create your views here.
