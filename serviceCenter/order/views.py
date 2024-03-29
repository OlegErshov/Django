from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import OrderItem
# from .forms import OrderCreateForm
from cart.cart import Cart
from services.models import Client
from .models import Order
from django.core.exceptions import PermissionDenied


def order_create(request):

    if not request.user.is_authenticated:
        raise PermissionDenied("net dostpa")

    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(client=Client.objects.filter(email=request.user.email).first())

        for item in cart:
            OrderItem.objects.create(order=order,
                                     issue=item['issue'],
                                     price=item['price'],)
            item['issue'].count += 1
            item['issue'].save()
        # очистка корзины
        cart.clear()
        return render(request, 'order/created.html',
                      {'order': order})

    return render(request, 'order/create.html',
                  {'cart': cart})

def list_orders(request):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied.")
    orders = Order.objects.all().order_by('client')
    return render(request, 'list_orders.html', {'orders': orders})