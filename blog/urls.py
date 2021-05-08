from django.urls import path
from .views import delete, detail, home, create, list, edit


urlpatterns = [
    path('', home, name="blog-home"),
    path('create/', create, name="blog-create"),
    path('list/', list, name="blog-list"),
    path('detail/<str:slug>', detail, name="blog-detail"),
    path('delete/<str:slug>', delete, name="blog-delete"),
    path('edit/<str:slug>', edit, name="blog-edit"),
]
