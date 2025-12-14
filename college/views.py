#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import College, Department, Program, Course, Staff, Student, Announcement

# Home Page
def home(request):
    announcements = Announcement.objects.all().order_by('-published_date')[:5]
    return render(request, 'college/home.html', {'announcements': announcements})

# Departments Page
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'college/departments.html', {'departments': departments})

# Programs Page
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'college/programs.html', {'programs': programs})

# Courses Page
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'college/courses.html', {'courses': courses})

# Staff Page
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'college/staff.html', {'staff_members': staff_members})

# Students Page
def student_list(request):
    students = Student.objects.all()
    return render(request, 'college/students.html', {'students': students})


# To Connect Departments to Home Page

def home(request):
    announcements = Announcement.objects.all().order_by('-published_date')[:5]
    departments = Department.objects.all()  # For interactive cards
    return render(request, 'college/home.html', {
        'announcements': announcements,
        'departments': departments
    })
