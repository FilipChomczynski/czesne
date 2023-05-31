import time
from django.shortcuts import redirect


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
