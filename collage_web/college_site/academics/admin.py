from django.contrib import admin
from .models import College, Department, Program, Course

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("name", "established_year")
    search_fields = ("name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "college")
    list_filter = ("college",)
    search_fields = ("name",)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "level")
    list_filter = ("level", "department")
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "program")
    search_fields = ("code", "title")
