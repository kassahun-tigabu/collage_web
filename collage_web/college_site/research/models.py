from django.db import models
from academics.models import Department

class ResearchProject(models.Model):
    STATUS_CHOICES = [
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
    ]

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="research_projects"
    )
    title = models.CharField(max_length=250)
    lead_researcher = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    #summary = models.TextField( )

    summary = models.TextField(default="Not provided")  # ✅ FIX

    def __str__(self):
        return self.title


class Publication(models.Model):
    PUBLICATION_TYPE = [
        ("Journal", "Journal Article"),
        ("Conference", "Conference Paper"),
        ("Book", "Book Chapter"),
    ]

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="publications"
    )
    research_project = models.ForeignKey(
        ResearchProject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="publications"
    )
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    publication_type = models.CharField(max_length=50, choices=PUBLICATION_TYPE)
    journal_or_conference = models.CharField(max_length=200)
    year = models.IntegerField()
    doi_or_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
