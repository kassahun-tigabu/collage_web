from django.shortcuts import render
from .models import Announcement

def announcement_list(request):
    announcements = Announcement.objects.filter(is_active=True)
    return render(request, "content/announcement_list.html", {
        "announcements": announcements
    })
