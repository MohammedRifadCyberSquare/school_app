from django.shortcuts import render,redirect
from school_admin.models import *
from school_teacher.models import *
from .models import *

def admin_login(request):
    message = ''
    if request.method == 'POST':
        admin_id = request.POST['admin_id']
        password = request.POST['password']

        record = SchoolAdmin.objects.filter(admin_id = admin_id, password = password)
        if record:
            request.session['admin_id'] = record[0].admin_id
            return redirect('hm:hm_dashboard')
        else:
            message = 'User Name or Password Incorrect'
    return render(request,'school_student/admin_login.html', {'message': message})


def teacher_login(request):
    message = ''
    if request.method == 'POST':
        teacher_id = request.POST['teacher_id']
        password = request.POST['password']

        record = Teacher.objects.filter(teacher_id = teacher_id, password = password)

        if record:
            request.session['teacher_id'] = record[0].id
            request.session['teacher_name'] = record[0].teacher_name
            request.session['teacher_class'] = record[0].teacher_class
            request.session['division'] = record[0].division

            
            print('hhh')
            return redirect('teacher:home')

        else:
            print('here')
            message = 'User Name or Password Incorrect'
    return render(request,'school_student/teacher_login.html', {'message': message})

def student_login(request):
    message = ''
    if request.method == 'POST':
        student_id = request.POST['admission_id']
        password = request.POST['password']
    
        record = Student.objects.filter(admission_no = student_id, password = password)
        if record:
            request.session['student_id'] = record[0].id
            request.session['student_name'] = record[0].student_name
            request.session['student_class'] = record[0].student_class
            request.session['division'] = record[0].division
            return redirect('student:home')
        else:
            message = 'User Name or Password Incorrect'
    return render(request,'school_student/student_login.html', {'message': message})


def home(request):
    return render(request,'school_student/home.html')

def notes(request):
    notes = Notes.objects.filter(student_cls = request.session['student_class'])
    return render(request,'school_student/view_notes.html',{'notes': notes})
