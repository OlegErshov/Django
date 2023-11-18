from django.shortcuts import render
from .models import Device_type, Issue,News,FeedBack, Stuff,BannerChangeTimer,PromoCode
from .forms import DeviceForm, IssueForm, FeedBackForm
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from cart.forms import CartIssueAddForm
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests

# def index(request):
#     return render(request, 'services/mainPage.html')


def services(request):
    devices = Device_type.objects.all()

    return render(request, 'services/ourServices.html', {'devices': devices})


def all_devices(request):
    device_types = Device_type.objects.all()
    news = News.objects.all()

    if (request.method == "POST" and request.user.is_superuser):
            time = BannerChangeTimer.objects.get(id=1)
            time.milliseconds = request.POST.get('milliseconds')
            time.save()
    
    time = BannerChangeTimer.objects.get(id=1)
    quote = requests.get('https://favqs.com/api/qotd').json()

    return render(request, 'services/mainPage.html',
                  {'Device_type': device_types,
                   'News': news,
                   'milliseconds': time.milliseconds,
                   'quote': quote['quote']['body']})

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

def issue_edit(request,id):
    if not request.user.is_staff:
        raise PermissionDenied("Net dostupa")
    try:
        issue = Issue.objects.get(id=id) # problem because id - device-id

        form = IssueForm(initial={'issue_type': issue.issue_type, 'price': issue.price,
                                 'device_type': issue.device_type})

        if request.method == "POST":
            issue.title = request.POST.get('issue_type')
            print(request.POST.get('title'))
            issue.price = request.POST.get('price')
            issue.device_type = Device_type.objects.get(id=request.POST.get('device_type'))

            issue.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "services/edit.html", {"issue": issue, 'form': form})
    except issue.DoesNotExist:
        return HttpResponseNotFound("<h2>book not found</h2>")


def detail(request, id):
    device = Device_type.objects.get(id=id)
    issues = Issue.objects.filter(device_type__name=device.name)
    cart_form = CartIssueAddForm()

    sort_t = request.GET.get('sort')

    if (str(sort_t) == 'ascending'):
        issues = issues.order_by('price')
    elif (str(sort_t) == 'descending'):
        issues = issues.order_by('-price')


    data = {
        'device': device,
        'issues': issues,
        'cart_form':cart_form
    }
    return render(request, 'services/details.html', data)

def news(request):
    return render(request, "services/news.html", {"news": News.objects.all()})

def faq(request):
    return render(request, "services/faq.html")

def about_us(request):
    return  render(request,"services/about_us.html")

def contacts(request):
    workers = Stuff.objects.all()
    return render(request,"services/contacts.html",{'workers': workers})

def feed_back(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'MISTAKE'

    feed_backs = FeedBack.objects.all()

    form = FeedBackForm(request.POST)

    data = {
        'form': form,
        'feedbacks': feed_backs
    }
    return render(request, 'services/feedback.html', data)

def trash(request):
    return render(request,"services/Trash.html")

def promo_codes_view(request):
    promo_codes = PromoCode.objects.all()
    return render(request, "services/promo_codes.html", {'promo_codes': promo_codes})
