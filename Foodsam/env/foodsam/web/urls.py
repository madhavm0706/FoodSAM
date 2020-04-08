
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('#about',views.customerRegistration,name='CustomerRegistration'),
    path('#services',views.chefRegistration,name='ChefRegistration'),
    path('#portfolio',views.restaurantRegistration,name='RestaurantRegistration'),
    path('menu/',views.menulist,name='menu'),
]