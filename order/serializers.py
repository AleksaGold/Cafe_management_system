from rest_framework.serializers import ModelSerializer

from item.serializers import ItemSerializer
from order.models import Order


class OrderSerializer(ModelSerializer):
    """Сериализатор для модели Order."""

    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "table_number",
            "items",
            "total_price",
            "status",
            "created_at",
        )


class OrderUpdateSerializer(ModelSerializer):
    """Сериализатор для обновления экземпляров модели Order."""

    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "table_number",
            "items",
            "status",
        )
