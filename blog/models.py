from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class BlogCategory(models.Model):
    name = models.CharField(max_length=275)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True, max_length=75)
    content = models.TextField(blank=False, null=False)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs', null=True, blank=False)
    image = CloudinaryField('image', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    blogpost = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    body = models.TextField(validators=[MinLengthValidator(4)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"