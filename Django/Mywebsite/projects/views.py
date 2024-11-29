from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Project, Review, Tag
from .forms import ProjectForm

def projects(request):
    projectsList = Project.objects.all()
    context = {'projectsList':projectsList}
    return render(request, "projects/projects.html", context )

def project(request, pk):

    # projectObj = None
    # for project in projectsList:
    #     if project['id'] == pk:
    #         projectObj = project 

    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    return render(request, "projects/single-project.html",{'projectObj':projectObj, "tags":tags} )


def createProject(request):
    form = ProjectForm
    context = {
        'form' : form
    }
    return render(request, "projects/project_form.html", context)