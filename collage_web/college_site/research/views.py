from django.shortcuts import render
from .models import ResearchProject, Publication

def research_overview(request):
    projects = ResearchProject.objects.all()
    publications = Publication.objects.all()

    return render(request, "research/research_overview.html", {
        "projects": projects,
        "publications": publications
    })


def publication_list(request):
    publications = Publication.objects.order_by("-year")
    return render(request, "research/publication_list.html", {
        "publications": publications
    })
