from django.urls import path
from .views import deletephoto, gallery, galleryedit, upload

urlpatterns = [
    path('', upload, name="upload-image"),
    path('list/', gallery, name='photos'),
    path('edit/<str:slug>', galleryedit, name='update-image'),
    path('delete/<str:slug>', deletephoto, name='delete-image'),

]
