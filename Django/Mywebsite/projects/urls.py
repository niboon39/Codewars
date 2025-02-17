from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name="projects"), 
    path("project/<str:pk>", views.project, name="project"),  # Dynamic page (name will link to html)
    path("create-project/", views.createProject, name="create-project"), 
]