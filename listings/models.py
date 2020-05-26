from django.db import models
from datetime import datetime
from realtors.models import Realtor

states_list = (
    ('Lagos', 'Lagos'),
    ('Abuja', 'Abuja'),
    ('Rivers', 'Rivers'),
    ('Anambra', 'Anambra'),
    ('Plateau', 'Plateau'),
    ('Ekiti', 'Ekiti'),
    ('0gun', 'Ogun'),
    ('Delta', 'Delta'),
    ('Kano', 'Kano'),
    ('Enugu', 'Enugu'),
    ('Kaduna', 'Kaduna'),
    ('Katsina', 'Katsina'),
    ('Akwa Ibom', 'Akwa Ibom'),
    ('Cross River', 'Cross River'),
    ('Edo', 'Edo'),
    ('Imo', 'Imo'),
    ('Bayelsa', 'Bayelsa'),
)
property_intent = (
    ('For Sale', 'For Sale'),
    ('For Rent', 'For Rent'),
    ('Lease', 'Lease')
)


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=15, choices=states_list)
    zipcode = models.CharField(max_length=7)
    status = models.CharField(max_length=15, choices=property_intent)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    sqft = models.IntegerField()
    bedrooms = models.IntegerField()
    pool = models.IntegerField()
    garage = models.IntegerField()
    security = models.BooleanField(default=False)
    bathrooms = models.IntegerField()
    toilets = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    listing = models.ForeignKey(Listing,
                                on_delete=models.CASCADE,
                                related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Review by {self.name} on {self.listing}'
