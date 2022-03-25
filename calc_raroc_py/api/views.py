from rest_framework import viewsets
from rest_framework.response import Response
from calc_raroc_py.models import Fluxo, calculaRaroc
from .serializer import FluxoSerializer, calculaRarocSerializer


class FluxoViewSet(viewsets.ModelViewSet):
    serializer_class = FluxoSerializer

    def get_queryset(self):
        fluxo = Fluxo.objects.all()
        return fluxo


class calculaRarocViewSet(viewsets.ModelViewSet):
    serializer_class = calculaRarocSerializer

    def get_queryset(self):
        calculararoc = calculaRaroc.objects.all()
        return calculararoc
