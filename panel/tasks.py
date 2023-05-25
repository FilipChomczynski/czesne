from .models import Uczen, Status
from celery import shared_task


@shared_task
def add_status_every_month():
    students = Uczen.objects.all()
    for student in students:
        status = Status(
            tytul="CZESNE",
            uczen=student,
            kwota=student.czesne.do_zaplaty
        )
        student.naleznosc += status.kwota
        status.save()
        student.save()
        
    print("STATUSES ADDED.")
