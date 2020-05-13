from django.shortcuts import render,redirect
from .algorithms import lcs,sort
from django.contrib.auth.models import User
from user.models import projects,blogs
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def search_for_person(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['people']
        total_person = User.objects.all().order_by('username')
        search_count=0
        search_list = []
        max_match = 0
        for person in total_person:
            full_name = person.first_name+person.last_name
            lcs_val = lcs(str(full_name),value)
            max_match = max(max_match,lcs_val)
        if max_match>len(value)/2:
            for person in total_person:
                full_name = person.first_name + person.last_name
                person_tuple = (person,lcs(str(full_name),value))
                if(person_tuple[1]>int(max_match/2)):
                    search_list.append(person_tuple)
                    search_count+=1
        sort(search_list)
        final_search_list=[]
        for i in search_list:
            final_search_list.append(i[0])
        context_dict = {'result':final_search_list,'total_result':search_count,'search_result':value}
        return render(request, 'user/people.html',context_dict)
    else:
        return redirect('main-page')


@login_required
def search_for_projects(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['projects']
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
        return render(request, 'user/projects.html',context_dict)
    return render(request,'user/projects.html')


@login_required
def search_for_blogs(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['blogs']
        total_blogs = blogs.objects.all().order_by('title')
        search_count=0
        search_list = []
        max_match = 0
        for blog in total_blogs:
            lcs_val = lcs(str(blog.title),value)
            max_match = max(max_match,lcs_val)
        for blog in total_blogs:
            project_tuple = (blog,lcs(str(blog.title),value))
            if(project_tuple[1]>int(max_match/2) and project_tuple[1]>=int(len(value))/2):
                search_list.append(project_tuple)
                search_count+=1
        sort(search_list)
        final_search_list=[]
        for i in search_list:
            final_search_list.append(i[0])
        context_dict = {'result':final_search_list,'total_result':search_count,'search_result':value,}
        return render(request, 'user/blogs.html',context_dict)
    return render(request,'user/blogs.html')


def blog_details(request,key):
    blog = blogs.objects.get(pk=key)
    context_dict = {'blog':blog}
    return render(request,'user/detail-blogs.html',context_dict)


def profiles(request,key):
    alumni = User.objects.get(pk=key)
    context_dict = {'alumni':alumni}
    return render(request,'user/profiles.html',context_dict)