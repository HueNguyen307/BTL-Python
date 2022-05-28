from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from Product.models import *

from cart.cart import Cart


def add_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return render(request, 'queenok/cart_page.html')


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return render(request, 'queenok/cart_page.html')


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return render(request, 'queenok/cart_page.html')


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return render(request, 'queenok/cart_page.html')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'queenok/cart_page.html')


def cart_page(request):
    return render(request, 'queenok/cart_page.html')

