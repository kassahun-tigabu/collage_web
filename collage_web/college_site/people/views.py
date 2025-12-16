#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Staff, Student

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, "people/staff_list.html", {
        "staff_members": staff_members
    })


def student_list(request):
    students = Student.objects.all()
    return render(request, "people/student_list.html", {
        "students": students
    })
