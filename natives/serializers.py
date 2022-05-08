from rest_framework import serializers
from .models import Cohort, Native

class NativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Native
        fields = '__all__'

class CohortSerializer(serializers.ModelSerializer):
    cohort = serializers.SerializerMethodField()
    
    class Meta:
        model = Cohort
        fields = '__all__'

    def get_cohort(self, obj):
        return obj.cohort.name
