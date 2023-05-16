from django import forms


class DodanieUcznia(forms.Form):
    imie = forms.CharField(label="Imię", max_length=40)
    nazwisko = forms.CharField(label="Nazwisko", max_length=40)
    klasa = forms.ChoiceField(label="Klasa", choices=())
    email = forms.EmailField(label="Email")
    naleznosc = forms.FloatField(label="Należność", initial=0)
    czesne = forms.ChoiceField(label="Czesne", choices=())

    def __init__(self, *args, **kwargs):
        wybory_klasa = kwargs.pop('wybory_klasa', ())
        wybory_czesne = kwargs.pop('wybory_czesne', ())
        super().__init__(*args, **kwargs)
        self.fields['klasa'].choices = wybory_klasa
        self.fields['czesne'].choices = wybory_czesne

class DodanieStatusu(forms.Form):
    uczen = forms.ChoiceField(label="Uczeń", choices=())
    kwota = forms.FloatField(label="Kwota", initial=0)
    tytul = forms.CharField(label="Tytuł")

    def __init__(self, *args, **kwargs):
        wybory_uczen = kwargs.pop('wybory_uczen', ())
        super().__init__(*args, **kwargs)
        self.fields['uczen'].choices = wybory_uczen
