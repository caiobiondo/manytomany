from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Students, Modules
from .serializer import StudentsSerializer, ModulesSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        student = Students.objects.all()
        return student


class ModulesViewSet(viewsets.ModelViewSet):
    serializer_class = ModulesSerializer

    def get_queryset(self):
        module = Modules.objects.all()
        return module