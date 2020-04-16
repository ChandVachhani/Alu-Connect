from django.shortcuts import render,redirect
from user.models import projects
from user.forms import AddProjectForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
def alumni(request):
    return render(request,'alumni/main.html')

def addproject(request):
    if request.method == 'POST':
        add_project_form = AddProjectForm(request.POST)
        if add_project_form.is_valid():
            project_name = add_project_form.cleaned_data['project-name']
            project_link = add_project_form.cleaned_data['project-Link']
            project_description = add_project_form.cleaned_data['project-description']
            try:
                project = projects.objects.create(name=project_name,url=project_link,description=project_description)
                return redirect('alumni')
            except IntegrityError as error:
                add_project_form.add_error('student_username',error)
            return render(request,'alumni/main.html',{'add_project_form': add_project_form})
        else:
            return render(request, 'alumni/main.html', {'add_project_form': add_project_form})
    else:
        add_project_form = AddProjectForm()
        return render(request, 'alumni/main.html', {'add_project_form':add_project_form})