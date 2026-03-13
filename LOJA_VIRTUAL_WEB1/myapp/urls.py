from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("product/", views.product, name='product'),
    path("books/", views.books, name='books'),
]