from django.shortcuts import render,redirect
from user.models import projects, publications
from django.contrib.auth.models import User
from user.forms import AddProjectForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .algorithms import lcs,sort


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
