from django.urls import path
from .views import staff_list, student_list

urlpatterns = [
    path("staff/", staff_list, name="staff_list"),
    path("students/", student_list, name="student_list"),
]
