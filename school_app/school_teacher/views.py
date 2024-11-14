from django.shortcuts import render,redirect
from .models import *
from school_student.models import Notes
# Create your views here.
def home(request):
    return render(request,'teacher/home.html')

def add_student(request):
    message = ''
    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        admission_no = request.POST['admissionNo']
        student_name = request.POST['studentName'].lower()

        record = Student.objects.filter(admission_no = admission_no)

        if not record:
            _ = Student(roll_no=roll_no, 
                        admission_no=admission_no,
                         student_class=request.session['teacher_class'],
                         division=request.session['division'],
                         student_name = student_name
                         
                         ).save()
            message = 'Student Added Succesfully '

        else:
            message = 'Admission No Exist'
    return render(request, 'teacher/add_student.html', {'message': message})

def students_list(request):     
    students = Student.objects.filter(
        student_class= request.session['teacher_class'],
        division = request.session['division'],
        status = 'active'
        ).order_by('roll_no')
    return render(request, 'teacher/student_list.html', {'students_list': students})

def upload_notes(request):
    message = ''     
    if request.method =='POST':
        class_st = request.POST['cls']
        descr = request.POST['descr']
        file = request.FILES['file']
        subject = request.POST['sub']
        notes = Notes(
            subject = subject,
            description = descr,
            added_by = request.session['teacher_name'],
            student_cls = class_st,
            file = file

        )
        notes.save()
        message = "Notes added Succesfully"

    return render(request, 'teacher/upload_notes.html',{'message': message})