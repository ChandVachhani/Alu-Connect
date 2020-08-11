from django.contrib import admin
from django.urls import path
from user import views
from student import views as stu_views
urlpatterns = [
    path('',views.main_page,name='main-page'),
    path('login/', views.login,name='login'),
    path('student_signup/',views.SignUpStudent,name='student_signup'),
    path('alumni_signup/',views.SignUpAlumni,name='alumni_signup'),
    path('people',stu_views.search_for_person,name='search_for_person'),
    path('user/logout',views.logout_user,name='logout_user'),
    path('projects/',stu_views.search_for_projects,name='search_for_projects'),
    path('blogs/',stu_views.search_for_blogs,name='search_for_blogs'),
    path('blogs/<int:key>',stu_views.blog_details,name='blog-details'),
    path('profiles/<int:key>',stu_views.profiles,name='profiles'),
]