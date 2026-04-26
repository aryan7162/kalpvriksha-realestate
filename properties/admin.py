from django.contrib import admin
from .models import Property, Amenity, PropertyImage, City, Sublocation

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_featured', 'image')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Sublocation)
class SublocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'slug')
    list_filter = ('city',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'property_type', 'city', 'sublocation', 'status', 'is_featured')
    list_filter = ('status', 'property_type', 'city', 'sublocation', 'is_featured')
    search_fields = ('title', 'sublocation__name', 'city__name')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PropertyImageInline]
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'status', 'is_featured', 'is_urgent_sale')}),
        ('Property Info', {'fields': ('property_type', 'price', 'price_per_sqft', 'booking_amount', 'description')}),
        ('Details', {'fields': ('bedrooms', 'bathrooms', 'area_sqft', 'carpet_area', 'floor_no', 'total_floors', 'amenities')}),
        ('Location', {'fields': ('address', 'sublocation', 'city', 'pincode')}),
        ('Media', {'fields': ('main_image', 'video_url', 'floor_plan')}),
        ('Builder', {'fields': ('builder_name', 'builder_logo', 'rera_number', 'possession_date')}),
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')