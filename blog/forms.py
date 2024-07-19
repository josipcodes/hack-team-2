from django import forms
from django.forms.widgets import ClearableFileInput

from .models import BlogCategory, Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'excerpt', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title...',
                'style': 'padding: 4px; width: 100%;'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'A bit about the product...',
                'rows': 10,
                'style': 'padding: 10px; max-height: 500px; width: 100%;'
            }),
            'excerpt': forms.TextInput(attrs={
                'placeholder': 'Excerpt...',
                'style': 'padding: 4px; max-height: 250px; width: 100%;'
            }),
            'image': ClearableFileInput(attrs={
                'accept': 'image/*'
            }),
            'status': forms.Select(attrs={
                'style': 'padding: 4px; width: 100%;'
            }),
        }
        labels = {
            'title': 'Title:',
            'content': 'Content:',
            'excerpt': 'Excerpt:',
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # Set the initial value of the image field
        if self.instance and self.instance.image:
            self.fields['image_display'] = forms.ImageField(required=False, initial=self.instance.image, widget=forms.FileInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Share your thoughts...',
                'rows': 5, 'maxlength': '1000',
                'style': 'padding: 10px; max-height: 200px; width: 100%;'
            }),
        }
        labels = {
            'body': ''
        }