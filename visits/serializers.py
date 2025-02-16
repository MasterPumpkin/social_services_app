from rest_framework import serializers
from clients.models import Client
from employees.models import Employee
from .models import Visit
from clients.serializers import ClientSerializer # Import Client Serializer
from employees.serializers import EmployeeSerializer # Import Employee Serializer

class VisitSerializer(serializers.ModelSerializer):
    #pro zobrazení detailu klienta a zaměstnance
    client = ClientSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)
    #pro zápis ID
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), source='client', write_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)

    class Meta:
        model = Visit
        fields = '__all__'