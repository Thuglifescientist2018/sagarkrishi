"""sagar_krishi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from sagar_krishi.views import about, about_edit, home
from django.contrib import admin
from django.urls import path, include
from searches.views import search_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="main-home"),
    path('about/', about, name="about"),
    path('about/edit', about_edit, name="about-edit"),
    path('search/', search_view, name="search"),

    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls'))
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
