
from django.db import models

# Create your models here.

class UserContact(models.Model):
    """Model definition for UserContact."""

    name = models.CharField(
        "Nombre", max_length=50, 
        )

    email = models.EmailField(
        "E-mail", 
        max_length=254,
        blank=False,
        null=False,
        )

    phone = models.CharField(
        "Telefono", 
        max_length=50,
        blank=True,
        null=True,
        )

    company = models.CharField(
        "Empresa", 
        max_length=50,
        default="Personal",
        )

    message = models.TextField()

    class Meta:
        """Meta definition for UserContact."""

        verbose_name = 'UserContact'
        verbose_name_plural = 'UserContacts'

    def __str__(self):
        """Unicode representation of UserContact."""
        return f'{self.name} | perteneciente a: {self.company}'
