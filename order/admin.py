from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "table_number",
        "status",
        "total_price",
    )
    list_filter = ("status",)
