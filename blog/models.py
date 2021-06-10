from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # lte = lesser than oe equal to
        return self.filter(publish_date__gte=now)

    def search(self, query):
        lookup = (Q(title__icontains=query)
                  | Q(content__icontains=query)
                  | Q(slug__icontains=query)
                  | Q(user__username__icontains=query)
                  | Q(user__first_name__icontains=query)
                  | Q(user__last_name__icontains=query)
                  | Q(publish_date__icontains=query)
                  # or whatever

                  )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True,
                            null=False, max_length=255)
    content = RichTextField()
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    # very important to  set objects to BlogPostManager() in order to access that manager attribues(eg. functions) and other inbuilt features
    objects = BlogPostManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
