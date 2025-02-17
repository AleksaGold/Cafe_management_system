from django.db.models import Q, Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from order.forms import OrderForm
from order.models import Order
from order.services import get_total_price


class OrderCreateView(CreateView):
    """Представление для создания нового экземпляра модели Order."""

    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order:order_list")

    def form_valid(self, form):
        """Валидация формы и расчет общей стоимости заказа."""
        order = form.save()
        get_total_price(order)
        return super().form_valid(form)


class OrderDetailView(DetailView):
    """Представление для просмотра экземпляра модели Order."""

    model = Order


class OrderListView(ListView):
    """Представление для просмотра списка экземпляров модели Order."""

    model = Order
    context_object_name = "orders"


class OrderUpdateView(UpdateView):
    """Представление для редактирования экземпляра модели Order."""

    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order:order_list")

    def form_valid(self, form):
        """Валидация формы и расчет общей стоимости заказа."""
        order = form.save()
        get_total_price(order)
        return super().form_valid(form)


class OrderDeleteView(DeleteView):
    """Представление для удаления экземпляра модели Order."""

    model = Order
    success_url = reverse_lazy("order:order_list")


def search_order_view(request):
    """Представление для поиска заказов по номеру стола."""
    if request.method == "POST":
        searched = request.POST["searched"]
        orders = Order.objects.filter(
            Q(status__contains=searched) | Q(table_number__contains=searched)
        )
        return render(
            request, "order/search_order.html", {"searched": searched, "orders": orders}
        )
    else:
        return render(request, "order/search_order.html", {})


def revenue_view(request):
    """Представление для расчета выручки за определенную дату."""

    date = request.GET.get("date", now().date())
    total_revenue = (
        Order.objects.filter(status="оплачено", created_at__date=date).aggregate(
            total=Sum("total_price")
        )["total"]
        or 0
    )

    return render(
        request,
        "order/revenue.html",
        {"total_revenue": total_revenue, "selected_date": date},
    )
