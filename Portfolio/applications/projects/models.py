#from typing_extensions import Required
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.




class projects(models.Model):
    # Variables categorías
    HardwareDevelop = "1"
    SoftwareDevelop = "2"
    DataSciece = "3"
    MachineLearning = "4"
    ArtificialInteligence = "5"


    #
    CATEGORY_CHOICES = (
        (HardwareDevelop, "Desarollo de hardware"),
        (SoftwareDevelop, "Desarrollo de software"),
        (DataSciece, "Ciencia de datos"),
        (MachineLearning, "Machine Learning"),
        (ArtificialInteligence, "Inteligencia Artificial")
    )

    title = models.CharField(
        "Título", 
        max_length=50, 
        null=False, 
        unique=True
        )
    category = models.CharField(
        "Categoría", 
        max_length=1,
        choices=CATEGORY_CHOICES
        )
    date = models.DateField(
        "Fecha", 
        auto_now=False, 
        auto_now_add=False
        )
    resume = models.TextField(
        "Resumen",
        max_length=200
        )
    contenido = RichTextUploadingField(
        "Contenido", 
        )
    photo_1 = models.ImageField(
        "Foto 1", 
        upload_to="images/", 
        height_field=None, 
        width_field=None, 
        max_length=None,
        null = True,
        blank= True,
        )
    photo_2 = models.ImageField(
        "Foto 2", 
        upload_to="images/", 
        height_field=None, 
        width_field=None, 
        max_length=None,
        null = True,
        blank= True,
        )
    photo_3 = models.ImageField(
        "Foto 3", 
        upload_to="images/", 
        height_field=None, 
        width_field=None, 
        max_length=None,
        null = True,
        blank= True,
        )
    video_1 = models.FileField(
        "Video 1", 
        upload_to="videos/", 
        max_length=100,
        null = True,
        blank= True,
        )
    video_2 = models.FileField(
        "Video 2", 
        upload_to="videos/", 
        max_length=100,
        null = True,
        blank= True,
        )
    anexos = models.CharField(
        "Anexos", 
        max_length=50
        )
    code = models.URLField(
        "Código", 
        max_length=200, 
        unique = True
        )
    public = models.BooleanField(
        "Público", 
        default=True
        )
    Favorite = models.BooleanField(
        "Favorito", 
        default=False
        )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    
    def __str__(self):
        return f"{self.id} | {self.title}"

class dependency(models.Model):

    """Model definition for dependency."""

    name = models.CharField(
        "Nombre", 
        max_length=100, 
        null=False
        )
    country = models.CharField(
        "Pais", 
        max_length=50
        )
    city = models.CharField(
        "Ciudad", 
        max_length=50
        )
    email = models.EmailField(
        "E-mail", 
        max_length=254
        )
    address = models.CharField(
        "Dirección", 
        max_length=100
        )
    phone = models.CharField(
        "Telefono", 
        unique=True,
        max_length=20
        )

    class Meta:
        """Meta definition for dependency."""

        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'

    def __str__(self):
        """Unicode representation of dependency."""
        return f"{self.id} | {self.name}"


class rewards(models.Model):
    """Model definition for Rewards."""

    name = models.CharField(
        "Nombre", 
        max_length=50, 
        unique=True
        )
    date = models.DateField(
        "Fecha", 
        auto_now=False, 
        auto_now_add=False
        )
    dependency_name = models.ForeignKey(
        dependency, 
        on_delete=models.CASCADE
        )
    link = models.URLField("Link", max_length=200, blank = True)
    
    class Meta:
        """Meta definition for Rewards."""

        verbose_name = 'Reconocimiento'
        verbose_name_plural = 'Reconocimientos'

    def __str__(self):
        """Unicode representation of Rewards."""
        return f"{self.id} | {self.name}"
