from django.conf import settings

def branding(request):
    return {'SITE_LOGO': getattr(settings, 'SITE_LOGO_URL', '')}