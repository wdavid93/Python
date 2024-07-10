# models.py

# Importer le module models de Django
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from shop.settings import AUTH_USER_MODEL
# from shop.models import Product  # Assurez-vous que le modèle Product est défini dans votre application shop

# Définir le modèle Product pour représenter un produit dans la boutique
class Product(models.Model):
    name = models.CharField(max_length=200)  # Nom du produit
    slug = models.SlugField(max_length=128)
    description = models.TextField()  # Description du produit
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix du produit
    stock = models.IntegerField()  # Quantité en stock
    available = models.BooleanField(default=True)  # Disponibilité du produit
    created = models.DateTimeField(auto_now_add=True)  # Date de création du produit
    updated = models.DateTimeField(auto_now=True)  # Date de dernière mise à jour du produit
    image = models.ImageField(upload_to='products/', blank=True)  # Champ image pour les produits
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # Champ image pour les produits

    # Méthode pour retourner le nom du produit
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug}) 
    
# Modèle pour représenter une commande individuelle
class Order(models.Model):
    # L'utilisateur qui a passé la commande ( au lieu de user je met AUTH_USER_MODEL)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    # Le produit commandé
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # La quantité de ce produit
    quantity = models.IntegerField(default=1)
    # Indique si la commande a été passée
    ordered = models.BooleanField(default=False)

# La méthode __str__ permet de définir une représentation en chaîne de caractères de l'objet.
# Cela rend les objets de ce modèle plus lisibles et informatifs lorsqu'ils sont imprimés ou affichés dans l'admin de Django, par exemple.

# def __str__(self):
#     # Retourne une chaîne de caractères formatée qui décrit l'objet de manière compréhensible.
#     return f"{self.product.name} ({self.quantity})"

    def __str__(self):
        # Debugging: Print the product name to console
        print(f"Product name: {self.product.name}")  
        # Ensure product has a name before returning
        if self.product and self.product.name:
            return f"{self.product.name} ({self.quantity})"
        else:
            return "Product name not available"

# Modèle pour représenter un panier d'achat
class Cart(models.Model):
    # L'utilisateur qui possède le panier
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    # # Les produits dans le panier, avec leur quantité respective
    # products = models.ManyToManyField(Product, through='CartProduct')
    # Les articles orders dans le panier
    orders = models.ManyToManyField(Order)
    # Indique si le panier a été commandé
    ordered = models.BooleanField(default=False)
    # Date à laquelle le panier a été commandé
    ordered_date = models.DateTimeField(null=True, blank=True)

# La méthode __str__ permet de définir une représentation en chaîne de caractères de l'objet.
# Cela rend les objets de ce modèle plus lisibles et informatifs lorsqu'ils sont imprimés ou affichés dans l'admin de Django, par exemple.

    def __str__(self):
        # Retourne une chaîne de caractères formatée qui décrit l'objet de manière compréhensible.        
        return f"Cart of {self.user.username}"
