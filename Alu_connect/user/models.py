from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class college(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table='college'


class branch(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table='branch'


class roles(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table='roles'


# class user_profile(models.Model):
#     profile_img = models.ImageField()
#     college = models.ForeignKey(college, on_delete=models.CASCADE)
#     branch = models.ForeignKey(branch,on_delete=models.CASCADE)
#     description = models.TextField()
#     password = models.CharField(max_length=16,)
#     user_role = models.ManyToManyField(roles,through='user_roles')
#     class Meta:
#         db_table='user_profile'
#
#
# class user_roles(models.Model):
#     roles = models.OneToOneField(roles,on_delete=models.CASCADE)
#     user = models.OneToOneField(user_profile,on_delete=models.CASCADE)
#     class Meta:
#         db_table='user_roles'
#
#
# class tags(models.Model):
#     name = models.CharField(max_length=40)
#     class Meta:
#         db_table='tags'
#
#
# class projects(models.Model):
#     name = models.CharField(max_length=20)
#     url = models.URLField()
#     title = models.CharField(max_length=20)
#     description = models.TextField()
#     tags = models.ManyToManyField(tags,on_delete=models.CASCADE)
#     modified_date = models.DateField()
#     class Meta:
#         db_table='projects'
#
#
# class project_tags(models.Model):
#     tags = models.OneToOneField(tags,on_delete=models.CASCADE)
#     project = models.OneToOneField(projects,on_delete=models.CASCADE)
#     class Meta:
#         db_table='project_tags'
#
#
# class blogs(models.Model):
#     title = models.CharField(max_length=20)
#     author = models.ForeignKey(user_profile,on_delete=models.CASCADE)
#     content = models.TextField()
#     image = models.ImageField()
#     views = models.IntegerField()
#     tags = models.ManyToManyField(tags,through='blog_tags')
#     class Meta:
#         db_table='blogs'
#
#
# class blog_tags(models.Model):
#     tags=models.OneToOneField(tags,on_delete=models.CASCADE)
#     blog = models.OneToOneField(blogs,on_delete=models.CASCADE)
#
#
# class publications(models.Model):
#     title = models.CharField(max_length=20)
#     Description = models.CharField(max_length=20)
#     url = models.URLField()
#     tags = models.ManyToManyField(tags,on_delete=models.CASCADE)
#     class Meta:
#         db_table='publications'
#
#
# class publication_tags(models.Model):
#     tags = models.OneToOneField(tags,on_delete=models.CASCADE)
#     publications = models.OneToOneField(publications,on_delete=models.CASCADE)
#
#
# class skills(models.Model):
#     Skill = models.CharField(max_length=20)
#     class Meta:
#         db_table="skills"
#
#
# class connect(models.Model):
#     Junior = models.OneToOneField(user_profile,on_delete=models.CASCADE)
#     Alumni = models.OneToOneField(user_profile,on_delete=models.CASCADE)
#     class Meta:
#         db_table="connect"
#
#
# class company(models.Model):
#     name = models.CharField(max_length=20)
#     class Meta:
#         db_table="company"
#
#
# class InterviewExperience(models.Model):
#     companyName = models.ManyToManyField(company,on_delete=models.CASCADE)
#     class Meta:
#         db_table="InterviewExperience"
#
#
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
