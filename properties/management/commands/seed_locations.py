from django.core.management.base import BaseCommand
from properties.models import City, Sublocation
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with predefined cities and sublocations'

    def handle(self, *args, **options):
        data = {
            "Pune": [
                "Baner", "Wakad", "Hinjewadi", "Kharadi", "Viman Nagar", "Hadapsar",
                "Magarpatta", "Kothrud", "Aundh", "Pimpri", "Chinchwad",
                "Talegaon", "Bavdhan", "Undri", "Kondhwa"
            ],
            "Mumbai": [
                "Andheri", "Bandra", "Powai", "Borivali", "Thane", "Dadar",
                "Goregaon", "Malad", "Chembur", "Navi Mumbai", "Lower Parel",
                "Worli", "Colaba", "Kandivali", "Ghatkopar"
            ],
            "Bangalore": [
                "Whitefield", "Electronic City", "Sarjapur Road", "Marathahalli",
                "Indiranagar", "Koramangala", "Yelahanka", "Hebbal",
                "HSR Layout", "Jayanagar", "BTM Layout", "Bannerghatta Road",
                "Bellandur", "KR Puram", "Rajajinagar"
            ],
            "Gurugram": [
                "DLF Phase 1", "DLF Phase 2", "DLF Phase 3", "DLF Phase 4", "DLF Phase 5",
                "Sohna Road", "Golf Course Road", "Golf Course Extension Road",
                "Sector 29", "Sector 57", "Sector 62", "Palam Vihar",
                "Sushant Lok", "MG Road", "New Gurgaon"
            ],
            "Noida": [
                "Sector 15", "Sector 18", "Sector 62", "Sector 63", "Sector 75",
                "Sector 76", "Sector 78", "Sector 93", "Sector 137", "Sector 150",
                "Noida Extension", "Greater Noida", "Pari Chowk",
                "Knowledge Park", "Alpha Beta Gamma"
            ],
            "Lucknow": [
                "Gomti Nagar", "Gomti Nagar Extension", "Hazratganj", "Aliganj",
                "Indira Nagar", "Jankipuram", "Rajajipuram", "Alambagh",
                "Charbagh", "Mahanagar", "Vikas Nagar", "Faizabad Road",
                "Sultanpur Road", "Sitapur Road", "Ashiyana"
            ],
            "Delhi": [
                "Connaught Place", "Karol Bagh", "Rohini", "Dwarka", "Saket",
                "Lajpat Nagar", "Vasant Kunj", "Janakpuri", "Pitampura",
                "Rajouri Garden", "Mayur Vihar", "Preet Vihar",
                "South Extension", "Greater Kailash", "Hauz Khas"
            ]
        }

        for city_name, sublocations in data.items():
            city, created = City.objects.get_or_create(
                name=city_name,
                defaults={'slug': slugify(city_name)}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created city: {city_name}'))
            else:
                self.stdout.write(f'City already exists: {city_name}')

            for sub_name in sublocations:
                sub, sub_created = Sublocation.objects.get_or_create(
                    city=city,
                    name=sub_name,
                    defaults={'slug': slugify(sub_name)}
                )
                if sub_created:
                    self.stdout.write(self.style.SUCCESS(f'  - Created sublocation: {sub_name}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded locations'))
