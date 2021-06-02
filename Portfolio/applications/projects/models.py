from django.db import models

# Create your models here.




class projects(models.Model):
    # Variables categorías
    HardwareDevelop = "1"
    SoftwareDevelop = "2"
    DataSciece = "3"
    MachineLearning = "4"
    ArtificialInteligence = "5"


    #
    CATEGORY_CHOICES = [
        (HardwareDevelop, "Desarollo de hardware"),
        (SoftwareDevelop, "Desarrollo de software"),
        (DataSciece, "Ciencia de datos"),
        (MachineLearning, "Machine Learning"),
        (ArtificialInteligence, "Inteligencia Artificial")
    ]

    title = models.CharField("Título", max_length=50, required=True)
    category = models.CharField("Categoría", choices=CATEGORY_CHOICES)
    date = models.DateField("Fecha", auto_now=False, auto_now_add=False)
    contenido = models.CharField("Contenido", max_length=500)
    photos = models.ImageField("Fotos", upload_to=None, height_field=None, width_field=None, max_length=None)
    #videos = models.FileField()
    anexos = models.CharField("Anexos", max_length=50)
    link = models.URLField("Link", max_length=200)


