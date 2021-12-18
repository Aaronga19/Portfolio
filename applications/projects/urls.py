from django.urls import path
from . import views

app_name = "projects_app"

urlpatterns = [
    path(
        "projects/",
        views.ProjectsListView.as_view(),
        name="projects-list",
    ),
    path(
        "projects/<pk>/",
        views.ProjectsDetailView.as_view(),
        name="project-detail",
    )


]

