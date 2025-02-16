from rest_framework import serializers
from visits.models import Visit
from .models import Attendance
from visits.serializers import VisitSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    visit = VisitSerializer(read_only=True)
    visit_id = serializers.PrimaryKeyRelatedField(queryset=Visit.objects.all(), source='visit', write_only=True)
    class Meta:
        model = Attendance
        fields = '__all__'