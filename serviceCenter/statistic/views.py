from login.models import CustomUser
from django.shortcuts import render
from django.db.models import Sum, F
import matplotlib.pyplot as plt
from django.conf import settings
import numpy as np
from django.core.exceptions import PermissionDenied
from os import path

def statistics(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Permission denied")

    clients = CustomUser.objects.order_by('last_name', 'first_name')
    client_data = []

    for client in clients:
        orders = client.order_set.all()
        total_sales = orders.annotate(
            total_cost=Sum(F('items__quantity') * F('items__cost'))
        ).aggregate(total_sales=Sum('total_cost'))['total_sales']
        client_data.append(
            {'client': client, 'orders': orders, 'total_sales': total_sales})

    context = {'client_data': client_data}