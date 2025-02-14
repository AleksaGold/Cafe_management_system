from django.urls import path

from order.apps import OrderConfig

app_name = OrderConfig.name

urlpatterns = [
    path("",),
]