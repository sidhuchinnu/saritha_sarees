from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def stock(request):
    return render(request, 'stock.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'reg.html')

def login(request):
    return render(request, 'login.html')