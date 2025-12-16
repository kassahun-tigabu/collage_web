from django.db import models

class College(models.Model):
    name = models.CharField(max_length=200)
    vision = models.TextField()
    established_year = models.IntegerField()

    def __str__(self):
        return self.name


class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Program(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs")
    name = models.CharField(max_length=150)
    level = models.CharField(max_length=50)  # BSc, MSc, PhD
    duration_years = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="courses")
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    credit_hours = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"
