from django.contrib import admin
from .models import ResearchProject, Publication

@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "lead_researcher", "status")
    list_filter = ("department", "status")
    search_fields = ("title", "lead_researcher")
    ordering = ("-start_date",)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "publication_type", "year")
    list_filter = ("department", "publication_type", "year")
    search_fields = ("title", "authors")
    ordering = ("-year",)
