from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import DodanieUcznia
from .models import Klasa, Uczen, Czesne
# Create your views here.


def panel(request):
    zalogowano = request.session.get('zalogowany', False)
    if not zalogowano:
        return redirect('/login/')

    uczniowie = Uczen.objects.all()
    return render(request, "panel.html", {"uczniowie": uczniowie})


def dodaj_ucznia(request):
    zalogowano = request.session.get('zalogowany', False)
    if not zalogowano:
        return redirect("/login/")

    klasy = Klasa.objects.all()
    wybory_klasa = []
    for i in klasy:
        wybory_klasa.append((i.id, i.nazwa))
    wybory_klasa = tuple(wybory_klasa)

    czesne = Czesne.objects.all()
    wybory_czesne = []
    for i in czesne:
        wybory_czesne.append((i.id, i.nazwa))
    wybory_czesne = tuple(wybory_czesne)

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
