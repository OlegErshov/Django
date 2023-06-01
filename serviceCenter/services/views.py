from django.shortcuts import render


def index(request):
    return render(request, 'services/mainPage.html')


def services(request):
    return render(request, 'services/ourServices.html')
