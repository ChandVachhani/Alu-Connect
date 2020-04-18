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
]