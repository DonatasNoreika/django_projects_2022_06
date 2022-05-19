from django.shortcuts import render
from django.views import generic
from .models import (Project,
                     Client,
                     Employee,
                     Invoice,
                     Job)


# Create your views here.
class ProjectListView(generic.ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
