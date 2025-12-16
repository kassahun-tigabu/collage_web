from django.urls import path
from .views import research_overview, publication_list

urlpatterns = [
    path("", research_overview, name="research_overview"),
    path("publications/", publication_list, name="publication_list"),
]
