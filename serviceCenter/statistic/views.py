from login.models import CustomUser
from django.shortcuts import render
from django.db.models import Sum, F
import matplotlib.pyplot as plt
from django.conf import settings
import numpy as np
from django.core.exceptions import PermissionDenied
from order.models import Order,OrderItem
from os import path
from django.http import HttpResponseRedirect
from io import BytesIO
import base64
import matplotlib.pyplot as plt



def user_order_history(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You must be authorized")

    orders = Order.objects.filter(client_id=request.user.id)
    order_items = dict()
    for o in orders:
        order_items[o.id] = OrderItem.objects.filter(order_id=o.id)

    return render(
        request, "statistic/history.html", {"orders": orders, "order_items": order_items}
    )

def get_plot():
    x = [o.created for o in Order.objects.all()]
    y = []
    for el in x:
        orders_in_date = Order.objects.all().filter(created=el)
        for order in orders_in_date:
            quantity = sum([i.quantity for i in order.items.all()])
        y.append(quantity)

    plt.plot(x, y)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    return string.decode("utf-8")

def shop_analyzer(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is too weak")

    orders_cost = Order.objects.values_list("cost")

    total_income = 0
    total_count = 0

    for el in orders_cost:
        total_income += el[0]
        total_count += 1

    # most_valuable_product = Order.objects.order_by("purchase_count").first()
    # min_valuable_product = Order.objects.order_by("-purchase_count").first()
    plot = get_plot()
    return render(
        request,
        "statistic/analyze.html",
        {
            "total_income": total_income,
            "total_count": total_count,
            # "most_valuable_product": most_valuable_product,
            # "min_valuable_product": min_valuable_product,
            "plot": plot,
        },
    )




# def statistics(request):
#     if not request.user.is_superuser:
#         raise PermissionDenied("Permission denied")
#
#     clients = CustomUser.objects.order_by('last_name', 'first_name')
#     client_data = []
#
#     for client in clients:
#         orders = client.order_set.all()
#         total_sales = orders.annotate(
#             total_cost=Sum(F('items__quantity') * F('items__cost'))
#         ).aggregate(total_sales=Sum('total_cost'))['total_sales']
#         client_data.append(
#             {'client': client, 'orders': orders, 'total_sales': total_sales})
#
#     context = {'client_data': client_data}

