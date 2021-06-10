from gallery.models import Gallery
from about.forms import AboutModelForm
from about.models import About
from django.shortcuts import redirect, render
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    gallery = Gallery.objects.all().order_by("-pk")[:5]
    template_name = "main/index.html"
    context = {
        "gallery": gallery
    }
    return render(request, template_name, context)


def about(request):
    template_name = "about/about.html"
    about = About.objects.all().last()
    context = {"about": about}
    return render(request, template_name, context)


@staff_member_required
def about_edit(request):
    template_name = 'about/about_edit.html'
    about = About.objects.all().last()
    form = AboutModelForm(request.POST or None, instance=about)
    if form.is_valid():
        form.save()
        return redirect('/about')

    context = {"form": form}
    return render(request, template_name, context)
