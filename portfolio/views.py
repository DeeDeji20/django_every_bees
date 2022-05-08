from portfolio.models import Project
from portfolio.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    @action(detail = False, methods= ['get'])
    def call_person(self, request):
        return Response({})
