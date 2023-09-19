from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'entry_date', 'type_position', 'currency', 'entry_price', 'dollar_value', 'coin_value', 'notes']