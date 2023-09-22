from django.urls import path
from .import views

app_name = 'services'

urlpatterns = [
    path('', views.all_devices, name='home'),
    path('services', views.services, name="services"),
    path('create', views.create, name='create'),
    path('createIssue',views.create_issue,name='createIssue'),
    path('edit/<int:id>/',views.issue_edit,name='editIssue'),
    path('details/<int:id>/',views.detail,name='detail'),
    path('faq',views.faq,name='faq'),
    path('about_us',views.about_us,name='about_us'),
    path('news',views.news,name='news'),
    path('feedback',views.feed_back,name='feedback'),
    path('contacts',views.contacts,name='contacts')

]

