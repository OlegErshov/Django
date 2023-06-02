from django.http import HttpResponse
from django.views.generic.edit import FormView
from ..services.models import Client
from .forms import UserCreateForm

# Create your views here.

class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = '/auth/login/'

    template_name = 'register.html'
    print(123)

    def form_valid(self, form) -> HttpResponse:

        form.save()

        Client.objects.create(first_name=form.cleaned_data['first_name'],
                              last_name=form.cleaned_data['last_name'],
                              date_of_birth=form.cleaned_data['date_of_birth'],
                              email=form.cleaned_data['email'],
                              phone_number=form.cleaned_data['phone_number']).save()

        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form) -> HttpResponse:
        return super(RegisterFormView, self).form_invalid(form)