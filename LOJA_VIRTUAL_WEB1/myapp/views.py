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

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'Contact.html')

def use_terms(request):
    return render(request, 'use_terms.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def ebooks(request):
    return render(request, 'ebooks.html')

def kit_avancado(request):
    return render(request, 'kit_avancado.html')

def kit_iniciante(request):
    return render(request, 'kit_iniciante.html')