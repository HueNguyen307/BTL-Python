from django.shortcuts import render
from django.http import HttpResponse

from User.models import User


def Order(request):
    return render(request, 'queenok/checkout_page.html')


def CheckOut(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(pk=user_id)
        for i in cart:
            a = (int(cart[i]['price']))
            b = (int(cart[i]['quantity']))
            total = a * b
            order = Order(
                user=user,
                product=(str(cart[i]['name'])),
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                address=address,
                phone=phone,
                total=total
            )
            order.save()
        request.session['cart'] = {}
        return render(request, 'queenok/index.html')

    return render(request, 'queenok/index.html')


def Order(request):
    uid = request.session.get('_auth_user_id')
    users = User.objects.get(pk=uid)
    order = Order.objects.filter(user=users)
    context = {
        'order': order,
    }
    return render(request, 'queenok/checkout_page.html', context)
