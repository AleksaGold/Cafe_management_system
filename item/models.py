from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    """Модель Item для хранения информации о блюдах в меню кафе."""

    name = models.CharField(max_length=100, verbose_name="Название блюда", unique=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
