
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("staff_dashboard",staff_dashboard,name="staff_dashboard"),
    path("student_dashboard",student_dashboard,name="student_dashboard"),
    path('post', post_attendance, name='post'),
    # path('view/', view_attendance, name='view_attendance'),
]
