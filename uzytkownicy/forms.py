from django import forms


class Logowanie(forms.Form):
    nazwa = forms.CharField(label="Nazwa Użytkownika", max_length=40)
    haslo = forms.CharField(label="Hasło", max_length=40)
