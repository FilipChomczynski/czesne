from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import DodanieUcznia, DodanieStatusu
from .models import Klasa, Uczen, Czesne
from django.db.models import Sum
from .utils import check_login, find_all_tuple
# Create your views here.


def panel(request):
    check_login(request)

    uczniowie = Uczen.objects.all()
    return render(request, "panel.html", {"uczniowie": uczniowie})


def dodaj_ucznia(request):
    check_login(request)

    wybory_klasa = find_all_tuple(Klasa)
    wybory_czesne = find_all_tuple(Czesne)

    form = DodanieUcznia(wybory_klasa=wybory_klasa,
                         wybory_czesne=wybory_czesne)

    if request.method == 'POST':
        form = DodanieUcznia(request.POST, wybory_klasa=wybory_klasa,
                             wybory_czesne=wybory_czesne)
        if form.is_valid():
            klasa = Klasa.objects.filter(
                id=int(form.cleaned_data['klasa'])).first()
            czesne = Czesne.objects.filter(
                id=int(form.cleaned_data['czesne'])).first()
            uczen = Uczen(
                imie=form.cleaned_data['imie'],
                nazwisko=form.cleaned_data['nazwisko'],
                email=form.cleaned_data['email'],
                klasa=klasa,
                czesne=czesne
            )
            try:
                uczen.save()
            except:
                return HttpResponse("zle dane")

    return render(request, 'dodaj-ucznia.html', {"form": form})


def dodaj_status(request):
    check_login(request)

    uczniowie = Uczen.objects.all()
    wybory_uczen = []
    for i in uczniowie:
        wybory_uczen.append((i.id, i.imie + ' ' + i.nazwisko))
    wybory_uczen = tuple(wybory_uczen)

    form = DodanieStatusu(wybory_uczen=wybory_uczen)

    if request.method == 'POST':
        form = DodanieStatusu(request.POST, wybory_uczen=wybory_uczen)
        if form.is_valid():
            redirect("/panel/")

    return render(request, 'dodaj-status.html', {"form" : form})