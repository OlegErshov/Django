from django.shortcuts import render
from .models import Device
from .forms import DeviceForm

def index(request):
    return render(request, 'services/mainPage.html')


def services(request):
    devices = Device.objects.all()
    return render(request, 'services/ourServices.html', {'devices': devices})


def create(request):

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'MISTAKE'

    form = DeviceForm()

    data = {
        'form': form,

    }
    return render(request, 'services/create.html',data)
