from rest_framework.serializers import ModelSerializer

from item.models import Item


class ItemSerializer(ModelSerializer):
    """Сериализатор для модели Item."""

    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "price",
        )
