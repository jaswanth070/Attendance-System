from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Student, Staff
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def register(request):
    if request.method == "POST":
        usrname = request.POST.get("username")
        password = request.POST.get("password")
        full_name  = request.POST.get("full_name")
        acc_type = request.POST.get("type")
        phone = request.POST.get("phone")

        hashed_password = make_password(password=password)

        if(acc_type == "staff"):
            user = Staff.objects.create(username=usrname,password=hashed_password,full_name=full_name,phone=phone)
        elif(acc_type == "student"):
            user = Student.objects.create(username=usrname,password=hashed_password,full_name=full_name,phone=phone)

        if user is None:
            return redirect("/signup/")
        
        return redirect("/login/")
    return render(request,"signup.html")

def login_view(request):
    if request.method == "POST":
        usrname = request.POST.get("username")
        password = request.POST.get("password")

        staff = Staff.objects.filter(username=usrname).first()
        student = Student.objects.filter(username=usrname).first()

        if staff and check_password(password,staff.password):
            request.session['user_type'] = 'staff'
            # request.session['user_id'] = staff.id
            request.session['user_id'] = staff.id
            request.session['full_name'] = staff.full_name
            # return redirect('staff_dashboard')
            return redirect('post')
        elif student and check_password(password,student.password):
            request.session['user_type'] = 'student'
            request.session['user_id'] = student.id
            request.session['full_name'] = student.full_name
            return redirect('student_dashboard')
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})
    return render(request,'login.html')

def logout_user(request):
    request.session.flush()
    return redirect('/login/')  
