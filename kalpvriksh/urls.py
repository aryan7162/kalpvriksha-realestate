from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from properties import views as properties_views
from leads import views as leads_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Properties app (includes Home, Property List, About, etc.)
    path('', include('properties.urls')), 
    
    # Leads & Careers (Fix for 'careers' not found)
    path('lead-capture/', leads_views.lead_capture, name='lead_capture'),
    path('newsletter-subscribe/', leads_views.newsletter_subscribe, name='newsletter_subscribe'),
    path('careers/', leads_views.careers, name='careers'),
    path('thank-you/', leads_views.thank_you, name='thank_you'),
    path('leads/api/chatbot/', leads_views.chatbot_api, name='chatbot_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)