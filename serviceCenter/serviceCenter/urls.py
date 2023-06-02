
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('services.urls')),
     path('auth/', include('login.urls', namespace='login'))
]
