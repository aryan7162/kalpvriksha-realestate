from django.db import models

class Lead(models.Model):
    LEAD_SOURCES = (
        ('property_page', 'Property Page'),
        ('contact_form', 'Contact Form'),
        ('homepage', 'Homepage'),
        ('blog', 'Blog'),
        ('landing_page', 'Landing Page'),
        ('social_media', 'Social Media'),
        ('referral', 'Referral'),
    )
    
    LEAD_STATUS = (
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('proposal_sent', 'Proposal Sent'),
        ('negotiation', 'Negotiation'),
        ('won', 'Won'),
        ('lost', 'Lost'),
        ('junk', 'Junk'),
    )
    
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=15, db_index=True)
    
    # Lead Details
    source = models.CharField(max_length=20, choices=LEAD_SOURCES, default='contact_form')
    status = models.CharField(max_length=20, choices=LEAD_STATUS, default='new')
    interested_property = models.ForeignKey('properties.Property', on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    message = models.TextField()
    
    # Interest
    preferred_property_type = models.CharField(max_length=50, blank=True)
    preferred_locality = models.CharField(max_length=100, blank=True)
    preferred_bedrooms = models.IntegerField(blank=True, null=True)
    purchase_timeline = models.CharField(max_length=50, blank=True)
    
    # Tracking
    user_agent = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    referring_url = models.URLField(blank=True, null=True)
    utm_source = models.CharField(max_length=100, blank=True)
    utm_medium = models.CharField(max_length=100, blank=True)
    utm_campaign = models.CharField(max_length=100, blank=True)
    
    # Communication
    call_attempts = models.PositiveIntegerField(default=0)
    last_contacted = models.DateTimeField(blank=True, null=True)
    follow_up_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)
    
    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email', 'status']),
            models.Index(fields=['phone', 'status']),
        ]
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email