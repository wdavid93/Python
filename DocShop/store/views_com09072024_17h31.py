# views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from store.models import Order, Product, Cart

# Vue pour la page d'accueil
def index(request):
    # return HttpResponse( "bonjour")
    products = Product.objects.all()
    # Récupérer les produits mis en avant (vous pouvez personnaliser cette logique)
    # featured_products = Product.objects.filter(available=True)[:5]
    # Rendre le template index.html avec le contexte des produits mis en avant
    # return render(request, 'store/index.html', {'featured_products': featured_products})
    return render(request, 'store/index.html' ,  {'products': products})
# Vue pour la liste des produits (existant déjà dans votre projet)
# def product_list(request):
#     products = Product.objects.filter(available=True)
#     return render(request, 'shop/product/list.html', {'products': products})

def product_detail(request,slug):
    # products = Product.objects.filter(available=True)
    # return render(request, 'shop/product/list.html', {'products': products})
    # return HttpResponse( slug)
    product = get_object_or_404( Product, slug=slug)
    # return HttpResponse( f"{ product.name } - { product.price } ")
    return render(request, 'store/detail.html' ,  {'product': product}) 
  
def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user, ordered=False)
    order, created = Order.objects.get_or_create(user=request.user, product = product, ordered=False)
    if created: # Si le produit est absent du panier, ajout
        cart.orders.add(order)
        cart.save()
    else:    
        # Si le produit est déjà dans le panier, augmenter la quantité
        order.quantity += 1
        order.save()

    return redirect(reverse('product'), kwargs= {'slug':slug})

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


def view_cart(request):
    pass
# def view_cart(request):
#     cart = Cart.objects.filter(user=request.user, ordered=False).first()
#     if not cart:
#         cart_products = []
#     else:
#         cart_products = CartProduct.objects.filter(cart=cart)
#     return render(request, 'store/view_cart.html', {'cart_products': cart_products})
