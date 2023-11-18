from django.urls import path
from . import views

app_name = 'personal_account'

urlpatterns = [
    path('', views.personal_account, name='personal_account')
]