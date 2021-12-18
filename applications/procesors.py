from .projects.models import projects

# Process to recovery the filter of the link by PYTHON

def python_filter(request):
        # Consulta de busqueda
    pythonQuery = projects.objects.find_python()
    print(pythonQuery)
    return pythonQuery

