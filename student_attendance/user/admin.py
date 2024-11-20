from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.site_header = "Admin Pannel"
admin.site.site_title = "Admin Pannel"

class StudentAdmin(admin.ModelAdmin):
    list_display = ['username','full_name','assigned_staff','phone']
    list_filter = ['username','assigned_staff']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['username','full_name','phone']
    list_filter = ['username']

admin.site.register(Staff,StaffAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.unregister(User)

