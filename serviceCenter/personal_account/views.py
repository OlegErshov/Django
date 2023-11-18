from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from order.models import Order
from django.shortcuts import  get_object_or_404

@login_required(login_url='/login/signin/')
def personal_account(request):
    user = request.user
    return render(request, 'personal_account/personal_account.html', {'user': user})


