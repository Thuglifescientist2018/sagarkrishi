from django.db import models
from django import forms
from django.db.models import fields
from about.models import About


class AboutModelForm(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"

    def clean_main_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("main_title")
        # filter() returns obj in queryset while get() returns the object itself so we can't  use exclude pk in get method
        qs = About.objects.filter(main_title__iexact=title)
        if instance is not None:  # we ignore the old instance update the data due to which
            # we are not gonna be getting title already exists error i think slug updates fine after adding instance=obj in the update view
            qs = qs.exclude(pk=instance.pk)  # id = instance of id
        if qs.exists():
            raise forms.ValidationError(
                "This title has been already taken")
        return title
