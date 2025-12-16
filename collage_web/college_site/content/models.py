from django.db import models
from academics.models import College

class Announcement(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="announcements")
    title = models.CharField(max_length=200)
    message = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
