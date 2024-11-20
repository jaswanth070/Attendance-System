from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student_roll','student_name','date','status']
    list_filter = ['student','date']
    date_hierarchy = 'date'

    def student_roll(self,obj):
        return f"{obj.student.username}"
    def student_name(self,obj):
        return f"{obj.student.full_name}"
    
    

    
    
admin.site.register(Attendance,AttendanceAdmin)

