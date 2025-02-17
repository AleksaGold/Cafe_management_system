from django import forms

from order.models import Order


class OrderForm(forms.ModelForm):
    """Форма для создания или редактирования экземпляра модели Order."""

    class Meta:
        model = Order
        exclude = (
            "total_price",
            "created_at",
        )
