from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import DodanieUcznia, DodanieStatusu, Filter, StatusFilter
from .models import Klasa, Uczen, Czesne, Status
from .utils import find_all_tuple
from django.db.models import Q


def panel(request):
    if request.session.get('zalogowany') is None:
        return redirect("/login/")

    students = Uczen.objects.all()
    statuses = Status.objects.all()

    class_ = find_all_tuple(Klasa, ['nazwa'], insert_empty=True)
    tuition = find_all_tuple(Czesne, ['nazwa'], insert_empty=True)
    form = Filter(
        class_choices=class_,
        tuition_choices=tuition
    )
    form_status = StatusFilter()

    if request.method == 'POST':
        form = Filter(
            request.POST,
            class_choices=class_,
            tuition_choices=tuition
        )
        if form.is_valid():
            if form.cleaned_data['student'] != '':
                try:
                    students = students\
                        .filter(imie=form.cleaned_data['student'].split()[0])\
                        .filter(nazwisko=form.cleaned_data['student'].split()[1])
                except IndexError:
                    students = students\
                        .filter(Q(imie=form.cleaned_data['student'].split()[0]) | Q(nazwisko=form.cleaned_data['student'].split()[0]))

            if form.cleaned_data['class_'] != '-1':
                students = students.filter(klasa=form.cleaned_data['class_'])

            if form.cleaned_data['charge_from'] is not None:
                students = students.filter(naleznosc__gte=form.cleaned_data['charge_from'])

            if form.cleaned_data['charge_to'] is not None:
                students = students.filter(naleznosc__lte=form.cleaned_data['charge_to'])

            if form.cleaned_data['tuition'] != '-1':
                students = students.filter(czesne=form.cleaned_data['tuition'])

    return render(request, "panel.html", {
        "uczniowie": students,
        "form_student": form,
        "statuses": statuses,
        "form_status": form_status
    })


def status_filter(request):
    if request.method == "POST":
        statuses = Status.objects.all()
        form_status = StatusFilter(request.POST)
        class_ = find_all_tuple(Klasa, ['nazwa'], insert_empty=True)
        tuition = find_all_tuple(Czesne, ['nazwa'], insert_empty=True)
        form_student = Filter(
            class_choices=class_,
            tuition_choices=tuition
        )
        if form_status.is_valid():
            # if form.cleaned_data['student'] != '':
            #     students = None
            #     try:
            #         students = Uczen.objects.filter(
            #             imie=form.cleaned_data['student'].split()[0],
            #             nazwisko=form.cleaned_data['student'].split()[1]
            #         )
            #     except IndexError:
            #         students = students\
            #             .filter(Q(imie=form.cleaned_data['student'].split()[0]) |
            #                     Q(nazwisko=form.cleaned_data['student'].split()[0])
            #                     )

            if form_status.cleaned_data['amount_from'] is not None:
                statuses = statuses.filter(kwota__gte=form_status.cleaned_data['amount_from'])
            if form_status.cleaned_data['amount_to'] is not None:
                statuses = statuses.filter(kwota__lte=form_status.cleaned_data['amount_to'])

        return render(request, "panel.html", {
            "uczniowie": Uczen.objects.all(),
            "form_status": form_status,
            "form_student": form_student,
            "statuses": statuses
        })


def dodaj_ucznia(request):
    if request.session.get('zalogowany') is None:
        return redirect("/login/")

    wybory_klasa = find_all_tuple(Klasa, ['nazwa'])
    wybory_czesne = find_all_tuple(Czesne, ['nazwa'])

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
                czesne=czesne,
                naleznosc=int(form.cleaned_data['naleznosc'])
            )
            try:
                uczen.save()
            except:
                return HttpResponse("zle dane")

    return render(request, 'dodaj-ucznia.html', {"form": form})


def dodaj_status(request):
    if request.session.get('zalogowany') is None:
        return redirect("/login/")

    student_choices = find_all_tuple(Uczen, ['imie', 'nazwisko'])
    form = DodanieStatusu(wybory_uczen=student_choices)

    if request.method == 'POST':
        form = DodanieStatusu(request.POST, wybory_uczen=student_choices)
        if form.is_valid():
            student = Uczen.objects.filter(
                id=int(form.cleaned_data['uczen'])).first()

            status = Status(
                tytul=form.cleaned_data['description'],
                uczen=student,
                kwota=form.cleaned_data['kwota']
            )

            try:
                status.save()
            except:
                return HttpResponse("zle dane")

            student.naleznosc += status.kwota
            student.save()

    return render(request, 'dodaj-status.html', {"form": form})
