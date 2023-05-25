from django.urls import path
from . import views

urlpatterns = [
    path("", views.panel, name="panel"),
    path("dodaj-ucznia/", views.dodaj_ucznia, name="dodaj_ucznia"),
    path("dodaj-status/", views.dodaj_status, name="dodaj_status"),
    path("status/", views.status_filter, name="status"),
]
