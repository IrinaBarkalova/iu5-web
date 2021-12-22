from computers.models import PCModel
from rest_framework import serializers


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = PCModel
        # Поля, которые мы сериализуем
        fields = ["photo", "name", "screen", "CPU", "memory", "price"]
