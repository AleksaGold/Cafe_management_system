def get_total_price(order):
    """Функция для автоматического расчета общей стоимости заказа."""
    order.total_price = sum(item.price for item in order.items.all())
    order.save(update_fields=["total_price"])
