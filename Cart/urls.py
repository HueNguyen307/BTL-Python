from django.contrib import admin
from django.urls import path

from Cart import views

urlpatterns = [
    path('cart', views.cart_page),
    path('cart/add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),

]
