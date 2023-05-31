from django.contrib import admin
from .models import Klasa, Uczen, Czesne, Status, Settings

# Register your models here.
admin.site.register(Klasa)
admin.site.register(Uczen)
admin.site.register(Czesne)
admin.site.register(Status)
admin.site.register(Settings)
