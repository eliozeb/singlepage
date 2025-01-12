from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<int:num>', views.sections, name='section'),  # Changed from sections to section
]