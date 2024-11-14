from django.shortcuts import render
from school_teacher.models import Teacher 

def home(request):
    return render(request,'school_admin/home.html')

def add_teacher(request):
    message = ''
    if request.method == 'POST':
        teacher_id = request.POST['teacherId']
        teacher_name = request.POST['teacherName'].lower()
        cls = request.POST['cls']
        division = request.POST['division']
        section = request.POST['section']


        record = Teacher.objects.filter(teacher_id = teacher_id)

        if not record:
            _ = Teacher(teacher_id=teacher_id, teacher_name=teacher_name,
                         teacher_class=cls,
                         division=division,
                         password='alif@12345',
                         section = section,
                          
                         ).save()
            message = 'Teacher Added Succesfully '

        else:
            message = 'Teacher ID Exist'
    return render(request,'school_admin/add_teacher.html',{'message': message})

def teachers_list(request):
    if request.method == 'POST':
        if 'flt_class' in request.POST:
            print('hello')
        if 'flt_division' in request.POST:
            print('divisionnn')
        if 'flt_section' in request.POST:
            print('section')
    teachers_list = Teacher.objects.filter(staff_status = 'active')
    return render(request, 'school_admin/teachers_list.html',{'teachers_list': teachers_list})
