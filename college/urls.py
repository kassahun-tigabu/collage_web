from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department_list, name='departments'),
    path('programs/', views.program_list, name='programs'),
    path('courses/', views.course_list, name='courses'),
    path('staff/', views.staff_list, name='staff'),
    path('students/', views.student_list, name='students'),
]
