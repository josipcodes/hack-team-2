from django import forms
# from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
