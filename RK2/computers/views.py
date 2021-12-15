from django.shortcuts import render
from rest_framework import viewsets

from computers.models import PC, Display
from computers.serializers import PCSerializer, DisplaySerializer


class PCViewSet(viewsets.ModelViewSet):
    queryset = PC.objects.all()
    serializer_class = PCSerializer


class DisplayViewSet(viewsets.ModelViewSet):
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer


def report(request):
    return render(request, 'report.html', {'data': {
        'display': Display.objects.select_related('pc')
    }})
