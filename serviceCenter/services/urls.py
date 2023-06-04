from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_devices_view.as_view(), name='home'),
    path('services', views.services, name="services"),
    path('create', views.create, name='create'),
    path('createIssue',views.create_issue,name='createIssue')
]

