from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Zakaznik)
admin.site.register(Kategorie)
admin.site.register(Produkt)
admin.site.register(Objednavka)
admin.site.register(PolozkaObjednavky)