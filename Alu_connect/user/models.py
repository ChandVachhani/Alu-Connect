from django.db import models
from django.contrib.auth.models import User
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

class user_profile(models.Model):
    profile_img = models.ImageField()
    college = models.OneToOneField(college, on_delete=models.CASCADE)
    branch = models.OneToOneField(branch,on_delete=models.CASCADE)
    email = models.EmailField(max_length=254,on_delete=models.CASCADE)
    description = models.TextField()
    #password
    user_role = models.ManyToManyField(roles,through='user_roles')
    class Meta:
        db_table='user_profile'

class user_roles(models.Model):
    roles = models.OneToOneField(roles,on_delete=models.CASCADE)
    user = models.OneToOneField(user_profile,on_delete=models.CASCADE)
    class Meta:
        db_table='user_roles'

class tags(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table='tags'

class projects(models.Model):
    name = models.CharField(max_length=20)
    # url = 
    title = models.CharField(max_length=20)
    description = models.TextField()
    tag = models.ManyToManyField(tags,on_delete=models.CASCADE)
    modified_date = models.DateField()
    class Meta:
        db_table='projects'

class blogs(models.Model):
    title = models.CharField(max_length=20)
    author = models.OneToOneField(user_profile,on_delete=models.CASCADE)
    content = models.TextField()
    # views
    class Meta:
        db_table='blogs'

class publications(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)
    # url
    Tag = models.ManyToManyField(tags,on_delete=models.CASCADE)
    class Meta:
        db_table='publications'

class skills(models.Model):
    Skill = models.CharField(max_length=20)
    class Meta:
        db_table="skills"

class connect(models.Model):
    Junior = models.OneToOneField(user_profile,on_delete=models.CASCADE)
    Alumni = models.OneToOneField(user_profile,on_delete=models.CASCADE)
    class Meta:
        db_table="connect"

class company(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table="company"

class InterviewExperience(models.Model):
    companyName = models.ManyToManyField(company,on_delete=models.CASCADE)
    class Meta:
        db_table="InterviewExperience"

class achievement(models.Model):
    name = models.CharField(max_length=20)
    #link
    class Meta:
        db_table="achievement"

class OJList(models.Model):
    ojName = models.CharField(max_length=20)
    #
    class Meta:
        db_table="OJList"

