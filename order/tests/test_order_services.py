from decimal import Decimal

import pytest

from item.models import Item
from order.models import Order
from order.services import get_total_price


@pytest.mark.django_db
def test_get_total_price():
    """Тестирование автоматического расчета общей стоимости заказа."""

    item1 = Item.objects.create(name="Морковь", price=Decimal(100.00))
    item2 = Item.objects.create(name="Салат", price=Decimal(100.00))
    test_order = Order.objects.create(table_number=1)
    test_order.items.set([item1, item2])

    get_total_price(test_order)

    assert test_order.total_price == Decimal(200.00)
