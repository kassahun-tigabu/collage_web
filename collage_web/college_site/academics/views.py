#from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import College, Department, Program, Course

#College Overview (Landing for Academics)
def college_overview(request):
    colleges = College.objects.all()
    return render(request, "academics/college_overview.html", {
        "colleges": colleges
    })


#Department List (Per College)
def department_list(request, college_id):
    college = get_object_or_404(College, id=college_id)
    departments = college.departments.all()

    return render(request, "academics/department_list.html", {
        "college": college,
        "departments": departments
    })


#Program List (Per Department)
def program_list(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    programs = department.programs.all()

    return render(request, "academics/program_list.html", {
        "department": department,
        "programs": programs
    })


#Course List (Per Program)
def course_list(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    courses = program.courses.all()

    return render(request, "academics/course_list.html", {
        "program": program,
        "courses": courses
    })


# Single Course Detail (Optional but Professional)
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(request, "academics/course_detail.html", {
        "course": course
    })
