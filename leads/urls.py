from django.urls import path
from . import views

urlpatterns = [
    path('capture/', views.lead_capture, name='lead_capture'),
    path('newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
