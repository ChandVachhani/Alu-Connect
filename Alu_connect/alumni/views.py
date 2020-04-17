from django.shortcuts import render,redirect
from user.models import projects
from user.forms import AddProjectForm,EditProjectForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .functions import extract_projects

# Create your views here.
@login_required
def alumni(request):
    if request.POST:
        add_project_form = AddProjectForm(request.POST)
        if add_project_form.is_valid():
            project_name = add_project_form.cleaned_data['project_name']
            project_link = add_project_form.cleaned_data['project_Link']
            project_description = add_project_form.cleaned_data['project_description']
            project = projects.objects.create(name=project_name,url=project_link,description=project_description,alumni=request.user)
            return redirect('alumni')
        else:
            user_projects = extract_projects(request)

            context_dict = {'add_project_form': add_project_form, 'projects': user_projects}
            return render(request, 'alumni/main.html', context_dict)
    else:
        user_projects = extract_projects(request)
        user_projects = list(user_projects)
        add_project_form = AddProjectForm()
        edit_form_list = []
        for project in user_projects:
            form_dict = {'id':project.pk,'project_name':project.name,
                         'project_Link':project.url,
                         'project_description':project.description,}
            edit_form = EditProjectForm(form_dict)
            edit_form_list.append(edit_form)
        total_projects = extract_projects(request).count()
        context_dict = {'add_project_form':add_project_form,'projects':user_projects,'edit_form_list':edit_form_list,'total_projects':total_projects,'range':range(total_projects)}
        return render(request, 'alumni/main.html', context_dict)
