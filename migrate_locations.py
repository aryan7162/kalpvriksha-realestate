import os
import django
import sys

# Add the project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kalpvriksh.settings')
django.setup()

from properties.models import Property, City, Sublocation
from django.utils.text import slugify

def migrate_data():
    properties = Property.objects.all()
    print(f"Migrating {properties.count()} properties...")
    
    for prop in properties:
        # Migrate City
        if prop.city and not prop.city_fk:
            city_name = prop.city.strip()
            city, created = City.objects.get_or_create(
                name=city_name,
                defaults={'slug': slugify(city_name)}
            )
            prop.city_fk = city
            print(f"Assigned city {city.name} to property: {prop.title}")
        
        # Migrate Sublocation
        # We don't have sublocation_name in old data (it was locality)
        # Wait, I renamed locality to sublocation_name in models.py earlier
        if prop.sublocation_name and not prop.sublocation_fk:
            sub_name = prop.sublocation_name.strip()
            if prop.city_fk:
                sub, created = Sublocation.objects.get_or_create(
                    city=prop.city_fk,
                    name=sub_name,
                    defaults={'slug': slugify(sub_name)}
                )
                prop.sublocation_fk = sub
                print(f"Assigned sublocation {sub.name} to property: {prop.title}")
        
        prop.save()

    print("Migration completed.")

if __name__ == "__main__":
    migrate_data()
