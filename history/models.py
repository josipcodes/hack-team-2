from django.db import models
from cloudinary.models import CloudinaryField

class History(models.Model):
    event = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.event