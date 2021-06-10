from django.contrib.auth import logout
from django import http
from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost
from django.shortcuts import redirect, render
from .forms import BlogPostModelForm
from django.core.paginator import Paginator
from .seo.seo import metatagseo, description
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        template_name = "blog.html"
        return render(request, template_name)
    else:
        return redirect('list/')


def logOut(request):
    logout(request)
    return redirect('/')


@staff_member_required
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
    keywords = metatagseo(blog.content)
    content = blog.content.replace("<p>", "").replace('</p>', '')

    context = {
        "blog": blog,
        "keywords": keywords,
        "description": description(content),


    }
    return render(request, template_name, context)


@staff_member_required
def edit(request, slug):
    template_name = "edit.html"
    blog = BlogPost.objects.get(slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('/blog/list')
    context = {
        "form": form,
        "blog": blog
    }
    return render(request, template_name, context)


@staff_member_required
def delete(request, slug):
    template_name = "delete.html"
    blog = BlogPost.objects.get(slug=slug)
    if request.method == "POST":
        blog.delete()
        return redirect('/blog/list')
    context = {"blog": blog}
    return render(request, template_name, context)
