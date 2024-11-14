from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length = 50)
    teacher_class = models.IntegerField()
    division = models.CharField(max_length = 10)
    password = models.CharField(max_length = 30)
    section = models.CharField(max_length = 30)
    
    staff_status = models.CharField(max_length = 20, default = 'active')

    class Meta:
        db_table = "teacher"


class Student(models.Model):
    roll_no = models.IntegerField()
    admission_no = models.IntegerField()
    student_name = models.CharField(max_length = 50)
    student_class = models.IntegerField()
    division = models.CharField(max_length = 10)
    student_status = models.CharField(max_length = 20, default = 'active')
    password = models.CharField(max_length = 30, default = "12345")  
    # status = models.CharField(max_length=20, default = 'active')
    class Meta:
        db_table = "student"

