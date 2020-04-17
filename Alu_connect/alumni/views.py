from django.shortcuts import render,redirect
from user.models import projects
from user.forms import AddProjectForm,EditProjectForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .functions import extract_projects
from user.models import projects, publications
from django.contrib.auth.models import User
from user.forms import AddProjectForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .algorithms import lcs,sort


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
        


def search_for_person(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['search-result']
        total_person = User.objects.all().order_by('Username')
        search_count=0
        search_list = []
        max_match = 0
        for person in total_person:
            lcs_val = lcs(str(person.Username),value)
            max_match = max(max_match,lcs_val)
        for person in total_person:
            person_tuple = (person,lcs(str(person.Username),value))
            if(person_tuple[1]>int(max_match/2) and person_tuple[1]>=int(len(value))/2):
                search_list.append(person_tuple)
                search_count+=1
        sort(search_list)
        final_search_list=[]
        for i in search_list:
            final_search_list.append(i[0])
        context_dict = {'result':final_search_list,'total_result':search_count,'search_result':value}
        return render(request, 'alumni/main.html',context_dict)
    return render(request,'alumni/main.html')

def search_for_project(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['search-result']
        total_projects = projects.objects.all().order_by('name')
        search_count=0
        search_list = []
        max_match = 0
        for project in total_projects:
            lcs_val = lcs(str(project.name),value)
            max_match = max(max_match,lcs_val)
        for project in total_projects:
            project_tuple = (project,lcs(str(project.name),value))
            if(project_tuple[1]>int(max_match/2) and project_tuple[1]>=int(len(value))/2):
                search_list.append(project_tuple)
                search_count+=1
        sort(search_list)
        final_search_list=[]
        for i in search_list:
            final_search_list.append(i[0])
        context_dict = {'result':final_search_list,'total_result':search_count,'search_result':value}
        return render(request, 'alumni/main.html',context_dict)
    return render(request,'alumni/main.html')

def search_for_publication(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['search-result']
        total_publications = publications.objects.all().order_by('title')
        search_count=0
        search_list = []
        max_match = 0
        for publication in total_publications:
            lcs_val = lcs(str(publication.title),value)
            max_match = max(max_match,lcs_val)
        for publication in total_publications:
            publication_tuple = (publication,lcs(str(publication.title),value))
            if(publication_tuple[1]>int(max_match/2) and publication_tuple[1]>=int(len(value))/2):
                search_list.append(publication_tuple)
                search_count+=1
        sort(search_list)
        final_search_list=[]
        for i in search_list:
            final_search_list.append(i[0])
        context_dict = {'result':final_search_list,'total_result':search_count,'search_result':value}
        return render(request, 'alumni/main.html',context_dict)
    return render(request,'alumni/main.html')
