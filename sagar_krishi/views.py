from django.shortcuts import render 


def home(request):
    template_name = "main/index.html"
    return render(request, template_name)