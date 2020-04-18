from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class projects(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    description = models.TextField()    
    date_of_addition = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    date_of_completion = models.DateField()    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    #tag
    class Meta:
        db_table='projects'
    def __str__(self):
        return self.name

class publications(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField()    
    date_of_addition = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # tags = models.ManyToManyField(tags,on_delete=models.CASCADE)
    class Meta:
        db_table='publications'

class tags(models.Model):
    name = models.CharField(max_length=40)
    class Meta:
        db_table='tags'

class project_tags(models.Model):
    tag = models.ForeignKey(tags,on_delete=models.CASCADE)
    project = models.ForeignKey(projects,on_delete=models.CASCADE)
    class Meta:
        db_table='project_tags'

class publication_tags(models.Model):
    tags = models.OneToOneField(tags,on_delete=models.CASCADE)
    publications = models.OneToOneField(publications,on_delete=models.CASCADE)




class coding_platform(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table='coding_platform'


class coding_profile(models.Model):
    rating = models.IntegerField()
    profile_link = models.URLField()
    platform = models.ForeignKey(coding_platform, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table='coding_profile'




class branch(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table='branch'



class college(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table='college'



class roles(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        db_table='user_roles'


class user_profile(models.Model):
    profile_pic = models.ImageField(null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(branch,on_delete=models.CASCADE,null=True)
    college = models.ForeignKey(college, on_delete=models.CASCADE,null=True)   
    user_role = models.ForeignKey(roles,on_delete=models.CASCADE)
    class Meta:
        db_table='user_profile'



class blogs(models.Model):
    title = models.CharField(max_length=20)
    picture = models.ImageField()
    content = models.TextField()
    views = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # tags = models.ManyToManyField(tags,through='blog_tags')
    class Meta:
        db_table='blogs'

class comments(models.Model):
    description = models.TextField()
    date_added = models.DateField()
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table="comments"

class blog_tags(models.Model):
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey(tags, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table="blog_tags"

class skills(models.Model):
    skill = models.CharField(max_length=30)
    class Meta:
        db_table="skills"

class user_skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    skill = models.ForeignKey(skills, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table="user_skills"

class interview_type(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        db_table="interview_type"

class interview_experience(models.Model):
    interview_type = models.ForeignKey(interview_type, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table="interview_experience"

class rounds(models.Model):
    name = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    interview_exp = models.ForeignKey(interview_experience, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table="rounds"

class company(models.Model):
    name = models.CharField(max_length=20)
    interview_exp = models.ForeignKey(interview_experience, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table="company"


#*************************************************************************************************************

# class achievement(models.Model):
#     name = models.CharField(max_length=20)
#     #link
#     class Meta:
#         db_table="achievement"
#
#
# class OJList(models.Model):
#     ojName = models.CharField(max_length=20)
#     #
#     class Meta:
#         db_table="OJList"
#
