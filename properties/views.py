from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Property

def home(request):
    featured_properties = Property.objects.filter(status='published', is_featured=True)[:3]
    latest_properties = Property.objects.filter(status='published').order_by('-created_at')[:3]
    return render(request, 'home.html', {
        'featured_properties': featured_properties,
        'latest_properties': latest_properties
    })

def property_list(request):
    # Get all published properties
    properties = Property.objects.filter(status='published')
    
    # Proper city and sub-location (locality) filtering
    city = request.GET.get('city', '')
    locality = request.GET.get('locality', '')

    if city:
        properties = properties.filter(city__iexact=city)
        if locality:
            properties = properties.filter(locality__iexact=locality)
    elif locality:
        properties = properties.filter(locality__iexact=locality)
    
    # Search functionality
    search_query = request.GET.get('q')
    if search_query:
        properties = properties.filter(
            Q(title__icontains=search_query) |
            Q(locality__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(city__icontains=search_query)
        )
    
    # Filter by property type
    property_type = request.GET.get('type')
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    # Filter by bedrooms
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        if bedrooms == '4':
            properties = properties.filter(bedrooms__gte=4)
        else:
            properties = properties.filter(bedrooms=bedrooms)
    
    # Filter by price range
    min_price = request.GET.get('min_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
    
    max_price = request.GET.get('max_price')
    if max_price:
        properties = properties.filter(price__lte=max_price)
    
    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    allowed_sorts = ['price', '-price', 'area_sqft', '-area_sqft', 'created_at', '-created_at']
    if sort_by in allowed_sorts:
        properties = properties.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(properties, 12)  # Show 12 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique localities for filter
    localities = Property.objects.filter(status='published').values_list('locality', flat=True).distinct()[:20]
    
    cities = ['Pune', 'Mumbai', 'Bangalore', 'Gurugram', 'Noida', 'Delhi', 'Lucknow']
    
    context = {
        'properties': page_obj,
        'search_query': search_query,
        'selected_city': city,
        'selected_locality': locality,
        'selected_type': property_type,
        'selected_bedrooms': bedrooms,
        'min_price': min_price,
        'max_price': max_price,
        'localities': localities,
        'cities': cities,
        'property_types': Property.PROPERTY_TYPES,
    }
    return render(request, 'properties/property_list.html', context)

def get_cities(request):
    """API to return unique city list."""
    cities = list(Property.objects.filter(status='published').values_list('city', flat=True).distinct().order_by('city'))
    return JsonResponse({'cities': cities})

def get_localities(request):
    """API to return sub-locations (localities) for a specific city."""
    city = request.GET.get('city')
    localities = list(Property.objects.filter(status='published', city__iexact=city).values_list('locality', flat=True).distinct().order_by('locality'))
    return JsonResponse({'localities': localities})

def property_detail(request, slug):
    property = get_object_or_404(Property, slug=slug, status='published')
    
    # Increment view count
    property.views_count += 1
    property.save(update_fields=['views_count'])
    
    # Get similar properties
    similar_properties = Property.objects.filter(
        status='published',
        property_type=property.property_type
    ).exclude(id=property.id)[:4]
    
    context = {
        'property': property,
        'similar_properties': similar_properties,
    }
    return render(request, 'properties/property_detail.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def faq(request):
    return render(request, 'faq.html')