from django.db import models

NULLABLE = {"blank": True, "null": True}


class Order(models.Model):
    """Модель Order для хранения информации о заказах."""

    TABLES_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
    ]

    STATUS_CHOICES = [
        ("в ожидании", "В ожидании"),
        ("готово", "Готово"),
        ("оплачено", "Оплачено"),
    ]

    table_number = models.PositiveSmallIntegerField(
        choices=TABLES_CHOICES, verbose_name="Номер стола"
    )
    items = models.ManyToManyField(
        "item.Item",
        verbose_name="Список заказанных блюд с ценами",
        related_name="items",
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Общая стоимость заказа",
        **NULLABLE,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="В ожидании",
        verbose_name="Статус заказа",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания заказа"
    )

    def __str__(self):
        return f"Заказ: {self.pk} стол: {self.table_number} общая стоимость: {self.total_price}, статус: {self.status}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
