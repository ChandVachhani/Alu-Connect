from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('',views.main_page,name='main-page'),
    path('login/', views.login,name='login'),
    path('alu/',views.alumni,name='alumni'),
    path('student_signup/',views.SignUpStudent,name='student_signup'),
    path('alumni_signup/',views.SignUpAlumni,name='alumni_signup'),
]