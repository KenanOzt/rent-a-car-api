from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'  # Tüm alanları (brand, model, price vs.) otomatik çevir