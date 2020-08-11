from django.contrib import admin
from .models import roles,projects,user_profile,skills,user_skills,interview_experience,interview_type,college,branch,company,coding_platform
# Register your models here.

admin.site.register(roles)
admin.site.register(projects)
admin.site.register(user_profile)
admin.site.register(skills)
admin.site.register(user_skills)
admin.site.register(interview_experience)
admin.site.register(interview_type)
admin.site.register(college)
admin.site.register(branch)
admin.site.register(company)
admin.site.register(coding_platform)