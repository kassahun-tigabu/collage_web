from django.urls import path
from .views import (
    college_overview,
    department_list,
    program_list,
    course_list,
    course_detail,
)

app_name = "academics"

urlpatterns = [
    path("", college_overview, name="college_overview"),
    path("college/<int:college_id>/", department_list, name="department_list"),
    path("department/<int:department_id>/", program_list, name="program_list"),
    path("program/<int:program_id>/", course_list, name="course_list"),
    path("course/<int:course_id>/", course_detail, name="course_detail"),
]
