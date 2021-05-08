from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True,
                            null=False, max_length=255)
    content = RichTextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
