from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class college(models.Model):
    name = models.CharField(max_length=100)

class branch(models.Model):
    name = models.CharField(max_length=100)
    college = models.OneToOneField(college,on_delete=models.CASCADE)

class roles(models.Model):
    name = models.CharField(max_length=20)

class user_profile(models.Model):
    profile_img = models.ImageField()
    branch = models.OneToOneField(branch,on_delete=models.CASCADE)
    description = models.TextField()
    user_role = models.ManyToManyField(roles,through='user_roles')

class user_roles(models.Model):
    roles = models.OneToOneField(roles,on_delete=models.CASCADE)
    user = models.OneToOneField(user_profile,on_delete=models.CASCADE)
