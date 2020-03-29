from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate
# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            identifier = login_form.cleaned_data['identifier']
            password = login_form.cleaned_data['password']
            # user = User.objects.get(username='dss06')
            user=authenticate(request,username=identifier,password=password)
            if user != None:
                login_user(request,user)
                return redirect('alumni')
            else:
                return redirect('login')

    else:
        login_form = LoginForm()
    return render(request,'user/login.html',{'form':login_form})

@login_required

def alumni(request):
    return render(request,'user/alumni.html')