"""
shop/urls.py : Ce fichier définit les routes spécifiques à l'application shop. 
Par exemple, la route pour la page d'accueil de l'application shop est définie comme path('', index, name='home').
"""

from django.urls import path # Importation de la fonction path depuis django.urls
from shop.views import index #, detail, checkout, confimation  # Importation de la vue index depuis shop.views

# Liste des URLs du projet
urlpatterns = [
    path('', index, name='home'),  # URL racine, utilise la vue index avec le nom 'home'
    # path('<int:myid>', detail, name="detail"),  # URL avec un paramètre entier myid, utilisant la vue detail avec le nom 'detail'
    # path('checkout', checkout, name="checkout"),  # URL 'checkout', utilise la vue checkout avec le nom 'checkout'
    # path('confirmation', confimation, name="confirmation" ),  # URL 'confirmation', utilise la vue confimation avec le nom 'confirmation'
]


