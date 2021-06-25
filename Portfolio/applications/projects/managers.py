from django.db import models
#from .models import projects

class ProjectsManager(models.Manager):
    """   Proccess to projects model    """


    def find_project(self, kword, category, language):
        # Proccess to find projects by category or a keyword
        if len(category)>0:
            return self.filter(
                category__icontains = category,
                title__icontains= kword,
                public = True,
            ).order_by('id')

        elif len(language)>0:
            return self.filter(
                languages__name = language,
                title__icontains= kword,                
                public = True
            ).order_by('id')

        else:
            return self.filter(
                title__icontains = kword,
                public = True,
            ).order_by('id')
    

