import time
from django.shortcuts import redirect
from .models import Uczen, Status, Czesne
from apscheduler.schedulers.blocking import BlockingScheduler
from celery.schedules import crontab
from celery.task import periodic_task


def check_login(request):
    logged = request.session.get('zalogowany', False)
    if not logged:
        return redirect("/login/")


def find_all_tuple(model, fields, insert_empty=False):
    all_objects = model.objects.all()
    choices = []

    for obj in all_objects:
        values = []
        for field in range(len(fields)):
            values.append(getattr(obj, fields[field]))
        choices.append((obj.id, ' '.join(values)))

    if insert_empty:
        choices.insert(0, (-1, "(żaden)"))

    return tuple(choices)


@periodic_task(run_every=crontab(hour=0, minute=0, seconds=1))
def add_status_every_month():
    students = Uczen.objects.all()
    for student in students:
        status = Status(
            tytul="CZESNE",
            uczen=student,
            kwota=student.czesne.nazwa
        )
        student.naleznosc += status.kwota
        status.save()
        student.save()


def execute_thread():
    time.sleep(60)
    scheduler = BlockingScheduler()
    scheduler.add_job(add_status_every_month, 'interval', minutes=1)
    scheduler.start()
