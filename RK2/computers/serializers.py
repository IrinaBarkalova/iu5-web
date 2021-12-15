from rest_framework import serializers

from computers.models import Display, PC


class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Display
        fields = "__all__"


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = "__all__"
