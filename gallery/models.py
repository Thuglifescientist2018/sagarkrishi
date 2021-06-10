from django.db import models

from django.utils.text import slugify

# Create your models here.


class Gallery(models.Model):
    image = models.ImageField(
        upload_to='image/gallery/', blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=255)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    subtitle = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)
