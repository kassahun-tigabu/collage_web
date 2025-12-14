#from django.db import models

# Create your models here.
from django.db import models


class College(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    established_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Department(models.Model):
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name='departments'
    )
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Program(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='programs'
    )
    name = models.CharField(max_length=150)
    level = models.CharField(
        max_length=50,
        choices=[
            ('BSc', 'Bachelor'),
            ('MSc', 'Master'),
            ('PhD', 'PhD')
        ]
    )
    duration_years = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.level})"


class Course(models.Model):
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    course_code = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    credit_hour = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course_code} - {self.title}"


class Staff(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='staff'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name='students'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    enrollment_year = models.PositiveIntegerField()

    def __str__(self):
        return self.student_id


class Announcement(models.Model):
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name='announcements'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
