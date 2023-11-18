
from django.contrib import admin
from django.urls import path, include

app_name = 'serviceCenter'

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('services.urls', namespace='services')),
     path('auth/', include('login.urls', namespace='login')),
     path('cart/', include('cart.urls', namespace='cart')),
     path('order/', include('order.urls', namespace='order')),
     path('statistic/', include('statistic.urls', namespace='statistic')),
     path('personal_account/',include('personal_account.urls',namespace= 'personal_account'))
]
