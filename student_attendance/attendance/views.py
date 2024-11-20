from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Attendance
from user.models import Student,Staff
from django.utils.timezone import now
from django.contrib import messages
from collections import defaultdict

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

def view_attendance(request):
    if request.session.get("user_type") == "staff":
        staff_id = request.session.get("user_id")
        students = Student.objects.filter(assigned_staff=staff_id)

        attendence_records = defaultdict(dict)
        for student in students:
            att_rec = Attendance.objects.filter(student=student)
            attendence_records[student.username] = [att_rec.filter(status="present").count(),len(att_rec)]
        print(attendence_records)
        return JsonResponse(attendence_records)
            
    elif request.session.get("user_type") == "student":
        student_id = request.session.get("user_id")
        att_rec = Attendance.objects.filter(student=student_id)
        attendence_records = [att_rec.filter(status="present").count(),len(att_rec)]
        return JsonResponse({"record":attendence_records})


    return render(request,"view_attendance.html")
           
