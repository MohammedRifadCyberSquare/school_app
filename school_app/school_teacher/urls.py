from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/student', views.add_student, name = 'add_student'),
    path('student/list', views.students_list, name = 'students_list'),
    path('notes/upload', views.upload_notes, name = 'upload_notes'),

     
]
