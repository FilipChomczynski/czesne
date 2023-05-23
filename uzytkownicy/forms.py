from django import forms


class Logowanie(forms.Form):
    nazwa = forms.CharField(label="Nazwa Użytkownika", max_length=40)
    haslo = forms.CharField(label="Hasło", max_length=40, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'
