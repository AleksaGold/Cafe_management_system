from django.urls import path

from rest_framework.routers import DefaultRouter

from order.apps import OrderConfig
from order.views import (OrderCreateView, OrderDeleteView, OrderDetailView,
                         OrderListView, OrderUpdateView, revenue_view,
                         search_order_view, OrderViewSet)

app_name = OrderConfig.name

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="orders")


urlpatterns = [
    path("order/create/", OrderCreateView.as_view(), name="order_create"),
    path("order/detail/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("order/list/", OrderListView.as_view(), name="order_list"),
    path("order/update/<int:pk>/", OrderUpdateView.as_view(), name="order_update"),
    path("order/delete/<int:pk>/", OrderDeleteView.as_view(), name="order_delete"),
    path("order/search/", search_order_view, name="order_search"),
    path("order/revenue/", revenue_view, name="order_revenue"),
]


urlpatterns += router.urls
