from django import template
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout_user
from panel.utils import check_login
from . import forms


def index(request):
    check_login(request)

    return redirect('panel/')


def login(request):
    print(request.session.get('zalogowany'))
    form = forms.Logowanie()
    if request.method == 'POST':
        form = forms.Logowanie(request.POST)
        if form.is_valid():
            user = User.objects.filter(
                username=form.cleaned_data['nazwa'])
            if user.exists():
                if user.first().check_password(form.cleaned_data['haslo']):
                    request.session['zalogowany'] = True
                    return redirect('/panel/')
                return HttpResponse("zle haslo")
            return HttpResponse("zly login")

    return render(request, "login.html", {"form": form})


def logout(request):
    request.session['zalogowany'] = None
    logout_user(request)
    return redirect('/login/')
