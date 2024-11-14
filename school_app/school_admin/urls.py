from django.urls import path
from . import views

app_name = 'school_admin'
urlpatterns = [
    path('', views.home, name = 'home'),   
    path('teacher/add', views.add_teacher, name = 'add_teacher'),   
    path('teachers/list', views.teachers_list, name = 'teachers_list')
     

]
