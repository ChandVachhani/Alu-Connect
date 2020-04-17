from user.models import projects

def extract_projects(request):
    return request.user.projects_set.all()