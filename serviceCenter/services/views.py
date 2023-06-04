from django.shortcuts import render
from .models import Device
from .forms import DeviceForm, IssueForm
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied

# def index(request):
#     return render(request, 'services/mainPage.html')


def services(request):
    devices = Device.objects.all()
    return render(request, 'services/ourServices.html', {'devices': devices})

class all_devices_view(ListView):
    model = Device
    template_name = 'services/mainPage.html'
    context_object_name = 'devices'

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


def create_issue(request):
    if not request.user.is_staff:
        raise PermissionDenied("Net dostupa")

    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'MISTAKE'

    form = IssueForm()

    data = {
        'form': form,

    }
    return render(request, 'services/create_issue.html', data)
