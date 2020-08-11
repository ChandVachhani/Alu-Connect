from django.contrib import admin
from django.urls import path
from alumni import views
urlpatterns = [
    path('',views.alumni,name='alumni'),
    path('add_blog/',views.add_blog_view,name='add-blog'),
    path('add_coding_profile/',views.add_coding_profile,name='add-coding-profile'),
]