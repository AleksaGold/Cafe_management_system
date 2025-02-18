from decimal import Decimal

import pytest
from rest_framework.test import APIClient

from item.models import Item
from order.models import Order

URL = "/order/orders/"  # URL для тестирования API


@pytest.fixture
def client():
    """Фикстура для создания экземпляра тестового API-клиента."""
    return APIClient()


@pytest.fixture
def sample_items():
    """Фикстура для создания экземпляров тестовых блюд."""
    item1 = Item.objects.create(name="Морковь", price=Decimal(100.00))
    item2 = Item.objects.create(name="Салат", price=Decimal(200.50))
    item3 = Item.objects.create(name="Горох", price=Decimal(500.00))
    return [item1, item2, item3]


@pytest.fixture
def sample_order(sample_items):
    """Фикстура для создания экземпляра тестового заказа."""
    order = Order.objects.create(
        table_number=1,
        total_price=Decimal(300.50),
        status="в ожидании",
    )
    order.items.set(sample_items[:2])
    return order
