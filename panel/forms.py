from django import forms
from django.utils.timezone import now


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
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'


class DodanieStatusu(forms.Form):
    uczen = forms.ChoiceField(label="Uczeń", choices=())
    kwota = forms.FloatField(label="Kwota", initial=0)
    description = forms.CharField(label="Opis")
    data = forms.DateTimeField(label="Data", initial=now)

    def __init__(self, *args, **kwargs):
        wybory_uczen = kwargs.pop('wybory_uczen', ())
        super().__init__(*args, **kwargs)
        self.fields['uczen'].choices = wybory_uczen
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'


class Filter(forms.Form):
    student = forms.CharField(label="Uczeń", max_length=60, required=False)
    class_ = forms.ChoiceField(label="Klasa", choices=())
    charge_from = forms.FloatField(label="Należność od", required=False)
    charge_to = forms.FloatField(label="Należność do", required=False)
    tuition = forms.ChoiceField(label="Czesne", choices=())

    def __init__(self, *args, **kwargs):
        student_choices = kwargs.pop('student_choices', ())
        class_choices = kwargs.pop('class_choices', ())
        tuition_choices = kwargs.pop('tuition_choices', ())
        super().__init__(*args, **kwargs)
        self.fields['class_'].choices = class_choices
        self.fields['tuition'].choices = tuition_choices
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'
