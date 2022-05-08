from natives.serializers import CohortSerializer, NativeSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cohort, Native

# Create your views here.
class NativeViewSet(viewsets.ModelViewSet):
    serializer_class = NativeSerializer
    queryset = Native.objects.all()

    @action(detail = False, methods= ['get'])
    def call_person(self, request):
        return Response({})

class CohortViewSet(viewsets.ModelViewSet):
   serializer_class = CohortSerializer
   queryset = Cohort.objects.all()

   @action(detail = False, methods=['get']) 
   def get_cohort_by_name(self, request):
       cohort_name = self.request.query_params.get('cohort_name')
       cohort = Cohort.objects.get(name = cohort_name)
       serializer = CohortSerializer(cohort)
       return Response(serializer.data)
 