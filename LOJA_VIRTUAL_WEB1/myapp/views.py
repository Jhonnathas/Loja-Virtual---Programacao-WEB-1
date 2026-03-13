from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def product(request):
    return render(request, 'product.html')

def books(request):
    return render(request, 'books.html')

def payment(request):
    return render(request, 'payment.html')