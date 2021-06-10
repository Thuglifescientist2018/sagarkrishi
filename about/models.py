from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class About(models.Model):
    main_title = models.CharField(max_length=255, null=True, blank=True)
    description = RichTextField()
    about_image = models.ImageField(upload_to="image/", blank=True, null=True)

    def __str__(self):
        return self.main_title
