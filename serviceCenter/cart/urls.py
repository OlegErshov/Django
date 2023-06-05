from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_details'),
    path('add/<int:book_id>/',
         views.cart_add,
         name='cart_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)