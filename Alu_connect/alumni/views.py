from django.shortcuts import render,redirect
from user.models import projects
from user.forms import EditProjectForm
from .functions import extract_projects
from user.models import projects, publications,blogs,coding_platform,coding_profile
from user.forms import AddProjectForm
from django.contrib.auth.decorators import login_required
from student.algorithms import lcs,sort
from .forms import add_blog

# Create your views here.
@login_required
def alumni(request):
    if request.POST:
        key = 'id'
        if key not in request.POST.keys():
            add_project_form = AddProjectForm(request.POST)
            if add_project_form.is_valid():
                project_name = add_project_form.cleaned_data['project_name']
                project_link = add_project_form.cleaned_data['project_Link']
                project_description = add_project_form.cleaned_data['project_description']
                project = projects.objects.create(name=project_name,url=project_link,description=project_description,user=request.user,start_date='2020-03-12',date_of_completion='2020-03-12')
                return redirect('alumni')
            else:
                user_projects = extract_projects(request)
                context_dict = {'add_project_form': add_project_form, 'projects': user_projects}
                return render(request, 'alumni/main.html', context_dict)
        else:
            edit_form = EditProjectForm(request.POST)
            if edit_form.is_valid():
                project_name = edit_form.cleaned_data['project_name']
                project_Link = edit_form.cleaned_data['project_Link']
                project_decription = edit_form.cleaned_data['project_description']
                project_id = edit_form.cleaned_data['id']
                project = projects.objects.get(pk=project_id)
                project.name = project_name
                project.url = project_Link
                project.description = project_decription
                project.save()
                return redirect('alumni')
    else:
        user_projects = extract_projects(request)
        user_projects = list(user_projects)
        add_project_form = AddProjectForm()
        all_blogs = blogs.objects.all()
        all_forms_list = []
        i=0
        for project in user_projects:
            form_dict = {'id':project.pk,'project_name':project.name,
                         'project_Link':project.url,
                         'project_description':project.description,}
            edit_form = EditProjectForm(form_dict)
            li = [user_projects[i], edit_form]
            all_forms_list.append(li)
            i+=1
        total_projects = extract_projects(request).count()
        all_coding_profiles = coding_profile.objects.filter(user=request.user)
        context_dict = {'add_project_form':add_project_form,'projects':all_forms_list,'total_projects':total_projects,'all_blogs':all_blogs,'all_coding_profiles':all_coding_profiles}
        return render(request, 'alumni/main.html', context_dict)


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

@login_required

def add_blog_view(request):
    if request.POST:
        add_blog_form = add_blog(request.POST,request.FILES)
        if add_blog_form.is_valid():
            title = add_blog_form.cleaned_data['blog_title']
            content = add_blog_form.cleaned_data['blog_content']
            image = add_blog_form.cleaned_data['blog_image']
            new_blog = blogs.objects.create(title=title,content=content,picture=image,views=0)
            return redirect('alumni')
        else:
            context_dict = {'form':add_blog_form}
            return render(request,'alumni/blogs.html',context_dict)
    else:
        add_blog_form = add_blog()
        context_dict = {'form':add_blog_form}
        return render(request,'alumni/blogs.html',context_dict)

@login_required

def add_coding_profile(request):
    if request.POST:
        rating = request.POST['rating_val']
        coding_url = request.POST['coding_url']
        coding_platform_id = request.POST['platform']
        add_coding_profile = coding_profile.objects.create(rating=rating,profile_link=coding_url,platform_id=coding_platform_id,user=request.user)
        return redirect('alumni')
    platforms = coding_platform.objects.all()
    context_dict = {'platforms':platforms}
    return render(request,'alumni/add_coding_profile.html',context_dict)