from django.contrib import admin
from .models import (
    College,
    Department,
    Program,
    Course,
    Staff,
    Student,
    Announcement
)

# ------------------ College ------------------
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'established_year')
    search_fields = ('name',)

# ------------------ Department ------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name', 'college__name')
    list_filter = ('college',)

# ------------------ Program ------------------
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level', 'duration_years')
    search_fields = ('name', 'department__name')
    list_filter = ('level', 'department')

# ------------------ Course ------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'program', 'credit_hour')
    search_fields = ('course_code', 'title', 'program__name')
    list_filter = ('program',)

# ------------------ Staff ------------------
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'department')
    search_fields = ('first_name', 'last_name', 'department__name')
    list_filter = ('department',)

# ------------------ Student ------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'program', 'enrollment_year')
    search_fields = ('student_id', 'first_name', 'last_name', 'program__name')
    list_filter = ('program', 'enrollment_year')

# ------------------ Announcement ------------------
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'college', 'published_date')
    search_fields = ('title', 'college__name')
    list_filter = ('college',)
    date_hierarchy = 'published_date'
