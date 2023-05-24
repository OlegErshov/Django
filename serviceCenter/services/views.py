from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Проверка связи половой</h4>")
