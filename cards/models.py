from django.db import models
from cloudinary.models import CloudinaryField

"""
Adding categories as choices,
given that only few categories should exist.
"""
CATEGORIES = (
    ("Flags", "Flags"),
    ("Did you know?", "Did you know?"),
    ("People", "People"),
    ("Glossary", "Glossary"),
    )

class Cards(models.Model):
    title = models.CharField(max_length=75, blank=False, null=False)
    content = models.CharField(max_length=200, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', null=True, blank=True)
    category = models.CharField(choices=CATEGORIES, null=False, blank=False, max_length=50)
    link = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
