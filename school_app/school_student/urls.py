from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.admin_login, name = 'admin_login'),
    path('student/home', views.home, name = 'home'),
    path('notes/list', views.notes, name = 'notes'),

    path('teacher/login', views.teacher_login, name = 'teacher_login'),
    path('student/login', views.student_login, name = 'student_login'),
    
]
