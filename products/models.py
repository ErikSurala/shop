from django.db import models

# Create your models here.
from django.db import models


class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=50)
    email = models.EmailField()
    mesto = models.CharField(max_length=50)

    def __str__(self):
        return self.jmeno


class Kategorie(models.Model):
    nazev = models.CharField(max_length=50)

    def __str__(self):
        return self.nazev


class Produkt(models.Model):
    nazev = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    sklad = models.IntegerField()
    poznamka = models.CharField(max_length=100, blank=True)

    kategorie = models.ForeignKey(
        Kategorie,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nazev


class Objednavka(models.Model):
    datum = models.DateField()

    zakaznik = models.ForeignKey(
        Zakaznik,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Objednavka {self.id}"


class PolozkaObjednavky(models.Model):
    objednavka = models.ForeignKey(
        Objednavka,
        on_delete=models.CASCADE
    )

    produkt = models.ForeignKey(
        Produkt,
        on_delete=models.CASCADE
    )

    mnozstvi = models.IntegerField()

    def __str__(self):
        return f"{self.produkt} - {self.mnozstvi}"