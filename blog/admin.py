from django.contrib import admin
from .models import BlogCategory, Blog, Comment
# Register your models here.

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):

    search_fields = ['name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'blogpost', 'created_on')
    search_fields = ('name', 'email', 'body')