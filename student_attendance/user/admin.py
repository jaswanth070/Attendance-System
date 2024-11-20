from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.site_header = "Admin Pannel"
admin.site.site_title = "Admin Pannel"

admin.site.register(Staff)
admin.site.register(Student)
admin.site.unregister(User)