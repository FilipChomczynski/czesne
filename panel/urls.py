from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.panel, name="panel"),
    path("dodaj-ucznia/", views.dodaj_ucznia, name="dodaj_ucznia")
]
