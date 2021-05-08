from blog.models import BlogPost
from .models import BlogPost
from django import forms


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        # if slug is displayed then it will not put the slug value from def save() from models.py
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Give a title to  your article'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Write about your article'}),
        }
        fields = ["title", "content"]
