from django.contrib import admin
from django.urls import path, include
from content.views import announcement_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", announcement_list, name="home"),

    path("academics/", include("academics.urls")),
    path("people/", include("people.urls")),
    path("research/", include("research.urls")),
    path("content/", include("content.urls")),
]
