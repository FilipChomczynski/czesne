from django.shortcuts import redirect

def check_login(request):
    zalogowano = request.session.get('zalogowany', False)
    if not zalogowano:
        return redirect("/login/")
    
def find_all_tuple(Model):
    all_objects = Model.objects.all()
    choices = []
    for i in all_objects:
        choices.append((i.id, i.nazwa))
    return tuple(choices)