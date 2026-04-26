from rest_framework import serializers
from .models import City, Sublocation

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'slug']

class SublocationSerializer(serializers.ModelSerializer):
    city_name = serializers.ReadOnlyField(source='city.name')
    
    class Meta:
        model = Sublocation
        fields = ['id', 'city', 'city_name', 'name', 'slug']
