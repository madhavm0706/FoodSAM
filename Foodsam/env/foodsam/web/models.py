from django.db import models

# Create your models here.
class CustomerRegistration(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    

class ChefRegistration(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
        


class RestaurantRegistration(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    
    