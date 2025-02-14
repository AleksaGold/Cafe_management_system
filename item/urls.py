from django.urls import path

from item.apps import ItemConfig

app_name = ItemConfig.name

urlpatterns = [
    path("",),
]