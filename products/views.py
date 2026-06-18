from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Produkt, Objednavka


def index(request):
    produkty = Produkt.objects.all()
    return render(request, 'products/index.html', {'produkty': produkty})


def prihlaseni(request):
    chyba = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('moje_objednavky')
        else:
            chyba = "Špatné jméno nebo heslo"

    return render(request, 'products/login.html', {'chyba': chyba})


def odhlaseni(request):
    logout(request)
    return redirect('index')


@login_required
def moje_objednavky(request):
    objednavky = Objednavka.objects.all()
    return render(request, 'products/moje_objednavky.html', {'objednavky': objednavky})