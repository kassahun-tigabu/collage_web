from django.contrib import admin
from .models import Staff, Student

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("full_name", "department", "role", "position")
    list_filter = ("role", "department")
    search_fields = ("full_name", "email")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "department", "enrollment_year")
    list_filter = ("department", "enrollment_year")
    search_fields = ("full_name", "student_id")

