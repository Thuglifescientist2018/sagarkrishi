
from blog.models import BlogPost
from django.shortcuts import render
from .forms import BlogPostModelForm
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    template_name = "blog.html"
    return render(request, template_name)


def create(request):
    template_name = "create.html"
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()

    context = {
        "form": form
    }
    return render(request, template_name, context)


def list(request):
    template_name = "list.html"
    blogs = BlogPost.objects.all()
    paginator = Paginator(blogs, 8)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blogs": page_obj
    }
    return render(request, template_name, context)


def detail(request, slug):
    template_name = "detail.html"
    blog = BlogPost.objects.get(slug=slug)
    context = {
        "blog": blog
    }
    return render(request, template_name, context)


def delete(request, slug):
    template_name = "delete.html"
    blog = BlogPost.objects.get(slug=slug)

    if request.POST == "submit":
        blog.delete()
    context = {"blog": blog}
    return render(request, template_name)


def edit(request, slug):
    template_name = "edit.html"
    blog = BlogPost.objects.get(slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=blog)
    context = {
        "form": form
    }
    return render(request, template_name, context)
