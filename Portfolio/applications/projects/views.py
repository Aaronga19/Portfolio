from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import projects

# Create your views here.



class ProjectsListView(ListView):
    model = projects
    template_name = "projects/list.html"
    context_object_name = 'projects'
    paginate_by = 4
    ordering = 'title'
    
    """def get_context_data(self, **kwargs):
        context = super(ProjectsListView, self).get_context_data(**kwargs)
        context["projects"] = projects.objects.all()
        return context"""
    

class ProjectsDetailView(DetailView):
    model = projects
    template_name = "projects/detail.html"
    context_object_name = 'projects'
