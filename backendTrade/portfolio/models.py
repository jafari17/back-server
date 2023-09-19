from django.db import models

# Create your models here.

class Portfolio(models.Model):
    entry_date = models.DateField()
    type_position = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    entry_price = models.DecimalField(max_digits=12, decimal_places=5)
    dollar_value = models.DecimalField(max_digits=12, decimal_places=5)
    coin_value = models.DecimalField(max_digits=12, decimal_places=5)
    notes = models.CharField(max_length=500, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency