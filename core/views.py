from django.shortcuts import render
from properties.models import Property

def home(request):
    # Get featured properties
    featured_properties = Property.objects.filter(status='published', is_featured=True)[:6]
    
    # Get latest properties
    latest_properties = Property.objects.filter(status='published').order_by('-created_at')[:6]
    
    context = {
        'featured_properties': featured_properties,
        'latest_properties': latest_properties,
    }
    return render(request, 'home.html', context)