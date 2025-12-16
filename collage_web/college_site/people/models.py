from django.db import models
from academics.models import Department


class Staff(models.Model):
    ACADEMIC = "Academic"
    ADMIN = "Admin"

    ROLE_CHOICES = [
        (ACADEMIC, "Academic Staff"),
        (ADMIN, "Administrative Staff"),
    ]

    full_name = models.CharField(max_length=150)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="staff"
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES
    )
    position = models.CharField(
        max_length=100,
        default="Lecturer"   # ✅ FIX
    )
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="students"
    )
    full_name = models.CharField(max_length=150)
    student_id = models.CharField(max_length=50, unique=True)
    enrollment_year = models.IntegerField()

    def __str__(self):
        return self.full_name
