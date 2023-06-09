from django.db import models
from django.utils import timezone
# Create your models here.


class Czesne(models.Model):
    nazwa = models.CharField(max_length=20)
    do_zaplaty = models.FloatField()

    def __str__(self):
        return self.nazwa


class Klasa(models.Model):
    nazwa = models.CharField(max_length=5)

    def __str__(self):
        return self.nazwa


class Uczen(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=40)
    email = models.EmailField()
    klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE)
    czesne = models.ForeignKey(Czesne, on_delete=models.CASCADE)
    naleznosc = models.FloatField(default=0)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Status(models.Model):
    tytul = models.CharField(max_length=50)
    uczen = models.ForeignKey(Uczen, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    kwota = models.FloatField()

    def __str__(self):
        return f"{self.tytul} {self.kwota}"


class Settings(models.Model):
    email = models.EmailField()
    email_subject = models.CharField(max_length=80)
    email_content = models.CharField(max_length=600)
    day_of_sending_email = models.CharField(max_length=2, default=1)
    day_of_adding_statuses = models.CharField(max_length=2, default=1)
