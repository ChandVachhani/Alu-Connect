from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.forms import LoginForm
from django.contrib.auth.models import User
from user.models import projects
from user.forms import StudentSignUpForm
from user.forms import AddProjectForm
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate,password_validation
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


def SignUp(request):
    if request.method == 'POST':
        signup_form = StudentSignUpForm(request.POST)
        if signup_form.is_valid():
            first_name = signup_form.cleaned_data['student_first_name']
            last_name = signup_form.cleaned_data['student_last_name']
            username = signup_form.cleaned_data['student_username']
            email = signup_form.cleaned_data['student_email']
            password = signup_form.cleaned_data['student_password']
            try:
                student = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                return redirect('login')
            except IntegrityError as error:
                signup_form.add_error('student_username',error)
            return render(request, 'user/signup.html', {'student_form': signup_form})
        else:
            return render(request, 'user/signup.html', {'student_form': signup_form})
    else:
        signup_form = StudentSignUpForm()
        return render(request,'user/signup.html',{'student_form':signup_form})


@login_required
def alumni(request):
    return render(request,'user/alumni.html')

def addproject(request):
    if request.method == 'POST':
        add_project_form = AddProjectForm(request.POST)
        if add_project_form.is_valid():
            project_name = add_project_form.cleaned_data['project-name']
            project_link = add_project_form.cleaned_data['project-Link']
            project_description = add_project_form.cleaned_data['project-description']            
            try:
                project = projects.objects.create_user(name=project_name,url=project_link,title=project_name)
                return redirect('alumni')
            except IntegrityError as error:
                add_project_form.add_error('student_username',error)
            return render(request, 'user/alumni.html', {'add_project_form': add_project_form})
        else:
            return render(request, 'user/alumni.html', {'add_project_form': add_project_form})
    else:
        add_project_form = AddProjectForm()
        return render(request,'user/alumni.html',{'add_project_form':add_project_form})