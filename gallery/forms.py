from django import forms
from django import forms
from django.forms import fields
from .models import Gallery


class GalleryModelForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ["image", "title", "subtitle"]

        def clean_title(self, *args, **kwargs):
            instance = self.instance
            title = self.cleaned_data.get("title")
            qs = Gallery.objects.filter(title__iexact=title)
            if instance is not None:  # we ignore the old instance update the data due to which
                # we are not gonna be getting title already exists error i think slug updates fine after adding instance=obj in the update view
                qs = qs.exclude(pk=instance.pk)  # id = instance of id
            if qs.exists():
                raise forms.ValidationError(
                    "This title has been already taken")
            return title
