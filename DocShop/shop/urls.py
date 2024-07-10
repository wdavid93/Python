"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import signup, logout_user, login_user
from store.views import add_to_cart, delete_cart, index, product_detail, cart
from django.conf.urls.static import static
from shop import settings

urlpatterns = [
    path('', index, name="index"),
        # URL pour la liste des produits, utilise la vue product_list
    # path('products/', views.product_list, name='product_list'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login') ,   
    path('logout/', logout_user, name='logout'),
    path('cart/', cart, name='cart'),
    path('cart/delete', delete_cart, name='delete-cart'),
    path('product/<str:slug>', product_detail, name = "product"),    
    path('product/<str:slug>/add-to-cart', add_to_cart, name = "add-to-cart"),    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# # urls.py
# from django.contrib import admin
# from django.urls import path
# from . import views


# urlpatterns = [
#     # URL pour la page d'accueil, utilise la vue index
#     path('', views.index, name='index'),
#     # URL pour la liste des produits, utilise la vue product_list
#     path('products/', views.product_list, name='product_list'),
# ]
