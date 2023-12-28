from django.shortcuts import render

def home(request):
    return render(request,'index1.html')

def inner(request):
    return render(request,'inner-page1.html')

def port(request):
    return render(request,'portfolio-details1.html')


# Create your views here.
