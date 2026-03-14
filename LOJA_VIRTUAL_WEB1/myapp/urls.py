from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("product/", views.product, name='product'),
    path("books/", views.books, name='books'),
    path("payment/", views.payment, name='payment'),
    path("about_us/", views.about_us, name='about_us'),
    path("contact/", views.contact, name='contact'),
    path("use_terms/", views.use_terms, name='use_terms'),
    path("privacy_policy/", views.privacy_policy, name='privacy_policy'),
    path("ebooks/", views.ebooks, name='ebooks'),
    path("kit_avancado/", views.kit_avancado, name='kit_avancado'),
    path("kit_iniciante/", views.kit_iniciante, name='kit_iniciante'),
]