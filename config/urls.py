from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("order", include("order.urls", namespace="order")),
    path("item", include("item.urls", namespace="item")),
    path("user/", include("users.urls", namespace="user")),
]
