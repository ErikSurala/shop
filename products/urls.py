from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.prihlaseni, name='login'),
    path('logout/', views.odhlaseni, name='logout'),
    path('moje-objednavky/', views.moje_objednavky, name='moje_objednavky'),
]