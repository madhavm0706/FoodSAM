from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import CustomerRegistration, ChefRegistration, RestaurantRegistration

# Create your views here.
def index(request):
    return render(request,'web/index.html')


def customerRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.get(username=username)
                context= {'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'web/index.html', context)
            except User.DoesNotExist:
                user = CustomerRegistration(username=username, password=password1, email=email, address=address)
                user.save(CustomerRegistration)
                context ={'error':'User Created'}
                return render(request,'web/index.html',context)

            
        else:


            context= {'error':'The passwords that you provided don\'t match'}
            return render(request,'web/index.html',context)  


def chefRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
       
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.get(username=username)
                context= {'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'web/index.html', context)
            except User.DoesNotExist:
                user = ChefRegistration(username=username, password=password1, email=email)
                user.save(ChefRegistration)
                context ={'error':'User Created'}
                return render(request,'web/index.html',context)

            
        else:


            context= {'error':'The passwords that you provided don\'t match'}
            return render(request,'web/index.html',context) 




def restaurantRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.get(username=username)
                context= {'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'web/index.html', context)
            except User.DoesNotExist:
                user = RestaurantRegistration(username=username, password=password1, email=email)
                user.save(RestaurantRegistration)
                context ={'error':'User Created'}
                return render(request,'web/index.html',context)

            
        else:


            context= {'error':'The passwords that you provided don\'t match'}
            return render(request,'web/index.html',context) 








def menulist(request):
	return render(request,'web/menu.html')