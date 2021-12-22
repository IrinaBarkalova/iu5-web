from rest_framework import viewsets
from computers.serializers import PCSerializer
from computers.models import PCModel


class PCViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = PCModel.objects.all().order_by('price')
    serializer_class = PCSerializer  # Сериализатор для модели