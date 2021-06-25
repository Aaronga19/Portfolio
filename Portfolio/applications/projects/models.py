#from typing_extensions import Required
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import ProjectsManager

# Create your models here.

class languages(models.Model):
    """Model definition for Languages."""

    name = models.CharField(
        'nombre', 
        max_length=20,
        unique=True,
        blank=False, 
        null=False
        )
    typed = models.BooleanField(
        'Tipado',
        blank=False,
        null = False
        )
    class Meta:
        """Meta definition for Languages."""

        verbose_name = 'Lenguaje'
        verbose_name_plural = 'Lenguajes'

    def __str__(self):
        """Unicode representation of Languages."""
        return f"{self.id} | {self.name}"

class framework(models.Model):
    """Model definition for Frameworks."""

    # TODO: Define fields here
    name = models.CharField(
        'nombre', 
        max_length=20,
        unique=True,
        blank=False, 
        null=False
        )
    class Meta:
        """Meta definition for Framework."""

        verbose_name = 'Framework'
        verbose_name_plural = 'Frameworks'

    def __str__(self):
        """Unicode representation of Frameworks."""
        return f"{self.id} | {self.name}"



class projects(models.Model):
    # Variables categorías
    HardwareDevelop = "1"
    SoftwareDevelop = "2"
    DataSciece = "3"
    MachineLearning = "4"
    ArtificialInteligence = "5"


    #
    CATEGORY_CHOICES = (
        (HardwareDevelop, "Hardware Developing"),
        (SoftwareDevelop, "Software Developing"),
        (DataSciece, "Data Sciece"),
        (MachineLearning, "Machine Learning"),
        (ArtificialInteligence, "Artificial Inteligence")
    )

    title = models.CharField(
        "Title", 
        max_length=200, 
        null=False, 
        unique=True
        )
    category = models.CharField(
        "Category", 
        max_length=1,
        choices=CATEGORY_CHOICES
        )
    date = models.DateField(
        "Date", 
        auto_now=False, 
        auto_now_add=False
        )
    resume = models.TextField(
        "Resume",
        max_length=200
        )
    contenido = RichTextUploadingField(
        "Content", 
        )
    photo_1 = models.ImageField(
        "Photo 1", 
        upload_to="images/", 
        height_field=None, 
        width_field=None, 
        max_length=None,
        null = False,
        blank= False,
        )
    photo_2 = models.ImageField(
        "Photo 2", 
        upload_to="images/", 
        height_field=None, 
        width_field=None, 
        max_length=None,
        null = True,
        blank= True,
        )
    photo_3 = models.ImageField(
        "Photo 3", 
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
        "Code", 
        max_length=200, 
        unique = True
        )

    languages = models.ManyToManyField(languages)

    frameworks = models.ManyToManyField(framework)

    public = models.BooleanField(
        "Public", 
        default=True
        )
    Favorite = models.BooleanField(
        "Favorite", 
        default=False
        )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return f"{self.id} | {self.title}"

    objects = ProjectsManager()

class dependency(models.Model):

    """Model definition for dependency."""

    name = models.CharField(
        "Name", 
        max_length=100, 
        null=False
        )
    country = models.CharField(
        "Country", 
        max_length=50
        )
    city = models.CharField(
        "City", 
        max_length=50
        )
    email = models.EmailField(
        "E-mail", 
        max_length=254
        )
    address = models.CharField(
        "Adress", 
        max_length=100
        )
    phone = models.CharField(
        "Phone", 
        unique=True,
        max_length=20
        )

    class Meta:
        """Meta definition for dependency."""

        verbose_name = 'Dependency'
        verbose_name_plural = 'Dependencies'

    def __str__(self):
        """Unicode representation of dependency."""
        return f"{self.id} | {self.name}"


class rewards(models.Model):
    """Model definition for Rewards."""

    name = models.CharField(
        "Name", 
        max_length=50, 
        unique=True
        )
    date = models.DateField(
        "Date", 
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

        verbose_name = 'Reward'
        verbose_name_plural = 'Rewards'

    def __str__(self):
        """Unicode representation of Rewards."""
        return f"{self.id} | {self.name}"


