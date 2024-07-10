# views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from store.models import Order, Product, Cart

# Vue pour la page d'accueil
def index(request):
    # Récupérer tous les produits
    products = Product.objects.all()
    # Rendre le template index.html avec le contexte des produits
    return render(request, 'store/index.html', {'products': products})

# Vue pour le détail d'un produit
def product_detail(request, slug):
    # Récupérer le produit correspondant au slug, ou renvoyer une 404 si non trouvé
    product = get_object_or_404(Product, slug=slug)
    # Rendre le template detail.html avec le contexte du produit
    return render(request, 'store/detail.html', {'product': product})

# Vue pour ajouter un produit au panier
def add_to_cart(request, slug):
    # Récupérer l'utilisateur actuel
    user = request.user
    # Récupérer le produit correspondant au slug, ou renvoyer une 404 si non trouvé
    product = get_object_or_404(Product, slug=slug)
    # Récupérer ou créer un panier non commandé pour l'utilisateur
    # on peut aussi ecrire : cart, _ = Cart.objects.get_or_create(user=request.user, ordered=False)
    cart, created = Cart.objects.get_or_create(user=request.user, ordered=False)
    # Récupérer ou créer une commande non commandée pour l'utilisateur et le produit
    order, created = Order.objects.get_or_create(user=request.user, product=product, ordered=False)
    if created:
        # Si la commande a été créée, l'ajouter au panier
        cart.orders.add(order)
        cart.save()
    else:
        # Si la commande existe déjà, augmenter la quantité
        order.quantity += 1
        order.save()
    
    # Rediriger vers la page de détail du produit
    return redirect(reverse('product', kwargs={'slug': slug}))


# # @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user, ordered=False)
    # cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    
    # if not created:
    #     # Si le produit est déjà dans le panier, augmenter la quantité
    #     cart_product.quantity += 1
    #     cart_product.save()
    
    # return redirect('view_cart')


def cart(request):
    cart = get_object_or_404(Cart, user=request.user) #Cart.objects.filter(user=request.user, ordered=False).first()
    return render(request, 'store/cart.html', context = {'orders': cart.orders.all()})

# def view_cart(request):
#     cart = Cart.objects.filter(user=request.user, ordered=False).first()
#     if not cart:
#         cart_products = []
#     else:
#         cart_products = CartProduct.objects.filter(cart=cart)
#     return render(request, 'store/view_cart.html', {'cart_products': cart_products})

# Vue pour supprimer le panier d'un utilisateur
def delete_cart(request):
    # Vérifie si l'utilisateur a un panier existant et assigne le panier à la variable cart
    if cart := request.user.cart:
        # Supprime toutes les commandes associées à ce panier
        cart.orders.all().delete()
        # Supprime le panier lui-même
        cart.delete()
    return redirect('index')    

#  def delete_cart_ancienne_facon(request):
#     cart = request.user.cart
#     if cart:
#         cart.orders.all().delete()
#         cart.delete()   
#     return redirect('index')    