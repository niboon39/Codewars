from django.forms import ModelForm
from .models import Project 

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__' # ['title', 'name'] we can spacific. 