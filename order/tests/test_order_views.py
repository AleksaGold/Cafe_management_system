from decimal import Decimal

import pytest
from rest_framework import status

from order.models import Order
from order.tests.conftest import URL


@pytest.mark.django_db
def test_order_items(sample_order):
    """ "Тестирование корректного количества и названия блюд в заказе."""

    assert sample_order.items.count() == 2
    item_names = list(sample_order.items.values_list("name", flat=True))

    assert "Морковь" in item_names
    assert "Горох" not in item_names


@pytest.mark.django_db
def test_order_create(sample_items):
    """ "Тестирование создания заказа."""

    order = Order.objects.create(
        table_number=2, status="в ожидании", total_price=Decimal(0)
    )
    order.items.set(sample_items)
    total_price = sum(item.price for item in sample_items)
    order.total_price = total_price
    order.save()

    assert order.items.count() == len(sample_items)
    assert order.total_price == total_price


@pytest.mark.django_db
def test_order_create(client):
    """Тестирование создания заказа (API)."""

    data = {
        "table_number": 1,
        "status": "в ожидании",
    }
    response = client.post(URL, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["table_number"] == 1


@pytest.mark.django_db
def test_order_list(client, sample_order):
    """Тестирование просмотра списка заказов (API)."""

    response = client.get(URL)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_order_retrieve(client, sample_order):
    """Тестирование просмотра одного заказа (API)."""

    url = f"{URL}{sample_order.id}/"
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["table_number"] == sample_order.table_number


@pytest.mark.django_db
def test_order_update(client, sample_order):
    """Тестирование обновления заказа (API)."""

    url = f"{URL}{sample_order.id}/"
    data = {"status": "готово"}
    response = client.patch(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["status"] == "готово"


@pytest.mark.django_db
def test_order_destroy(client, sample_order):
    """Тестирование удаления заказа (API)."""

    url = f"{URL}{sample_order.id}/"
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Order.objects.filter(id=sample_order.id).exists() is False
