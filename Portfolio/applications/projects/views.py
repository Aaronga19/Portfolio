from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import projects, languages
from django.utils import timezone
# Create your views here.



class ProjectsListView(ListView):
    model = projects
    template_name = "projects/list.html"
    context_object_name = 'projects'
    paginate_by = 4
    ordering = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(ProjectsListView, self).get_context_data(**kwargs)
        context["languages"] = languages.objects.all()
        
        categories={}
        for category in projects.CATEGORY_CHOICES[:]:
            categories.update({category[0]:category[1]})
        zipCat = zip(categories.values(), categories.keys())
        context["categories"] = zipCat
        return context
    
    def get_queryset(self):
        kword = self.request.GET.get("kword", "")
        category = self.request.GET.get("category", "")
        language = self.request.GET.get("language", "")
        # Consulta de busqueda
        resultado = projects.objects.find_project(kword, category, language)
        return resultado
    

class ProjectsDetailView(DetailView):
    model = projects
    template_name = "projects/detail.html"
    context_object_name = 'projects'
    
    
