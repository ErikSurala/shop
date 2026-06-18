from django.db import models


from django.contrib.auth.models import User

class Zakaznik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    id_zakaznik = models.BigAutoField(primary_key=True)
    jmeno = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mesto = models.CharField(max_length=50)

    def __str__(self):
        return self.jmeno


class Kategorie(models.Model):
    id_kategorie = models.BigAutoField(primary_key=True, db_column='id_kategorie')
    nazev = models.CharField(max_length=50)

    class Meta:
        db_table = 'products_kategorie'

    def __str__(self):
        return self.nazev


class Produkt(models.Model):
    id_produkt = models.BigAutoField(primary_key=True, db_column='id_produkt')
    nazev = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    sklad = models.IntegerField()
    poznamka = models.CharField(max_length=100, blank=True)

    id_kategorie = models.ForeignKey(
        Kategorie,
        on_delete=models.CASCADE,
        db_column='id_kategorie'
    )

    class Meta:
        db_table = 'products_produkt'

    def __str__(self):
        return self.nazev


class Objednavka(models.Model):
    id_objednavka = models.BigAutoField(primary_key=True, db_column='id_objednavka')
    datum = models.DateField()

    id_zakaznik = models.ForeignKey(
        Zakaznik,
        on_delete=models.CASCADE,
        db_column='id_zakaznik'
    )

    class Meta:
        db_table = 'products_objednavka'

    def __str__(self):
        return f"Objednavka {self.id_objednavka}"


class PolozkaObjednavky(models.Model):
    id_polozka = models.BigAutoField(primary_key=True, db_column='id_polozka')

    id_objednavka = models.ForeignKey(
        Objednavka,
        on_delete=models.CASCADE,
        db_column='id_objednavka'
    )

    id_produkt = models.ForeignKey(
        Produkt,
        on_delete=models.CASCADE,
        db_column='id_produkt'
    )

    mnozstvi = models.IntegerField()

    class Meta:
        db_table = 'products_polozkaobjednavky'

    def __str__(self):
        return str(self.mnozstvi)