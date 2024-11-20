from django.shortcuts import render,redirect
from .models import Attendance
from user.models import Student,Staff
from django.utils.timezone import now
from django.contrib import messages

# def post_attendance(request):
#     if request.session.get('user_type') != "staff":
#         return redirect('logout')

#     staff_id = request.session.get('user_id')
#     students = Student.objects.filter(assigned_staff=staff_id)
#     today = now().date()

#     if request.method == "POST":
#         for student in students:
#             attendance_status = request.POST.get(f'attendance_{student.id}', 'absent') 
#             Attendance.objects.update_or_create(
#                 student=student,
#                 date=today,
#                 defaults={"status": attendance_status}
#             )

#         messages.success(request, "Attendance updated successfully!")
#         return redirect('post')  

#     return render(request, 'attendance_post.html', {
#         "students": students
#     })
def post_attendance(request):
    if request.session.get("user_type") != "staff":
        return redirect("logout")
    staff_id = request.session.get("user_id")
    students = Student.objects.filter(assigned_staff=staff_id)

    today = now().date()

    if request.method == "POST":
        for student in students:
            attendance = request.POST.get(f"attendance_{student.id }","absent")
            Attendance.objects.update_or_create(student=student,date=today,defaults={"status": attendance})
        
        return redirect("post")
    return render(request,"attendance_post.html",{"students":students,"today":today})

def staff_dashboard(req):
    return render(req,"staff_dashboard.html")

def student_dashboard(req):
    return render(req,"student_dashboard.html")
