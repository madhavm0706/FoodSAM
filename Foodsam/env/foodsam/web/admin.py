from django.contrib import admin

from .models import CustomerRegistration, ChefRegistration, RestaurantRegistration

# Register your models here.
admin.site.register(CustomerRegistration)
admin.site.register(ChefRegistration)
admin.site.register(RestaurantRegistration)