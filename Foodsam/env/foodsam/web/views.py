from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def index(request):
    return render(request,'web/index.html')


def CustomerRegistration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(username=username).exits():
                messages.info(request,'Username already Taken')
                return render(request,'web/index.html')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email already Taken')
                 return render(request,'web/index.html')
            else:

                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
        else:
            messages.info(request,' Password Do not Match')
            return render(request,'web/index.html')


    else:

        return render(request,'web/index.html')    