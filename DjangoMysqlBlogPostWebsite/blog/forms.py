from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['slug']
        fields = ['title', 'content', 'slug'] 
