from django.shortcuts import render
from .forms import GalleryModelForm
from .models import Gallery
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


@staff_member_required
def upload(request):
    template_name = 'upload.html'
    form = GalleryModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form,

    }
    return render(request, template_name, context=context)


def gallery(request):
    template_name = 'gallery.html'
    gallery = Gallery.objects.all().order_by("-pk")
    context = {
        "gallery": gallery
    }
    return render(request, template_name, context)


def galleryedit(request, slug):
    template_name = "editgallery.html"
    gallery = Gallery.objects.get(slug=slug)
    form = GalleryModelForm(request.POST or None, instance=gallery)
    if form.is_valid():
        form.save()
    context = {"form": form, "gallery": gallery}
    return render(request, template_name, context=context)


def deletephoto(request, slug):
    template_name = "deletephoto.html"
    photo = Gallery.objects.get(slug=slug)
    if request.method == "POST":
        photo.delete()
    context = {
        "photo": photo
    }
    return render(request, template_name, context)
