from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('', views.login,name='login'),
    path('alu/',views.alumni,name='alumni')
]