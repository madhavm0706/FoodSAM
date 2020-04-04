from django.db import models

# Create your models here.
class CustomerRegistration(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
