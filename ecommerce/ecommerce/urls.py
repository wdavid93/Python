"""

ecommerce/urls.py : Ce fichier est le point d'entrée principal pour le routage des URL dans le projet Django. 
Il inclut les routes définies dans shop/urls.py via path('', include('shop.urls')). 
Cela signifie que toutes les routes définies dans shop/urls.py seront disponibles sous le chemin principal du projet.
ecommerce URL Configuration


Configuration des URL pour le projet ecommerce

La liste `urlpatterns` route les URLs vers les vues. Pour plus d'informations, voir :
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Exemples :
Vues basées sur des fonctions
    1. Ajouter une importation :  from my_app import views
    2. Ajouter une URL à urlpatterns :  path('', views.home, name='home')
Vues basées sur des classes
    1. Ajouter une importation :  from other_app.views import Home
    2. Ajouter une URL à urlpatterns :  path('', Home.as_view(), name='home')
Inclure une autre configuration d'URL
    1. Importer la fonction include() : from django.urls import include, path
    2. Ajouter une URL à urlpatterns :  path('blog/', include('blog.urls'))
"""

# Importation des modules nécessaires
from django.contrib import admin
from django.urls import path, include

# Définition des patterns d'URL pour le projet
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'interface d'administration de Django
    path('', include('shop.urls')),  # Inclusion des URLs de l'application 'shop'
]
