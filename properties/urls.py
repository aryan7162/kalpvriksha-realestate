from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('faq/', views.faq, name='faq'),
    path('<slug:slug>/', views.property_detail, name='property_detail'),
]