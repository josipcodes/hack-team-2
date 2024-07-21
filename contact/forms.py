from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    anonymous = forms.BooleanField(required=False, initial=False, label="I'd like to remain anonymous")

