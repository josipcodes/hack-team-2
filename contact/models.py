from django.db import models
from cloudinary.models import CloudinaryField


class Contact(models.Model):
    """
    CONTACT FORM, allows site
    visitors to write a message or query.
    """
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    message = models.TextField(max_length=350, blank=True)

    def __str__(self):
        return str(self.name)
