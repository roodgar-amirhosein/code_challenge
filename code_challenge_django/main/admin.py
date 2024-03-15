from django.contrib import admin
from .models import Orders


# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user', 'stock', 'display_status', 'creation_date', 'price', 'quantity']

    def display_status(self, obj):
        return obj.get_status_display()


admin.site.register(Orders, OrdersAdmin)
