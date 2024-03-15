from django.db import models
from choices import Users_Choice, Stock_Choices, Order_Status_Choices


# Create your models here.

class Orders(models.Model):
    user = models.CharField(max_length=10, choices=Users_Choice)
    stock = models.CharField(max_length=10, choices=Stock_Choices)
    status = models.CharField(max_length=15, choices=Order_Status_Choices)
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user}--{self.stock}--{self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name_plural = 'Orders'

