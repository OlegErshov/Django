from django.urls import path
from . import views

app_name = 'statistic'

urlpatterns = [

    path("history", views.user_order_history, name="history"),
    path("analyze", views.shop_analyzer, name="analyze")
]