from django.contrib import admin
from django.urls import path

from Order import views

urlpatterns = [
    path('checkout/', views.CheckOut, name='checkout'),
    path('order/', views.Order, name='order'),
]
