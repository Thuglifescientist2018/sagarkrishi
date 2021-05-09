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

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:  # we ignore the old instance update the data due to which
            # we are not gonna be getting title already exists error i think slug updates fine after adding instance=obj in the update view
            qs = qs.exclude(pk=instance.pk)  # id = instance of id
        if qs.exists():
            raise forms.ValidationError(
                "This title has been already taken")
        return title
