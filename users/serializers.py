from rest_framework import serializers
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth import authenticate
from employees.models import Employee

class LoginSerializer(serializers.Serializer):  # Inherit from Serializer, not ModelSerializer
    username = serializers.CharField()
    password = serializers.CharField()
    employee_id = serializers.IntegerField(read_only=True) # Add employee_id

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.')

            # Check if the user has a corresponding Employee
            try:
                employee = Employee.objects.get(username=user.username)

            except Employee.DoesNotExist:
                raise serializers.ValidationError('No employee found for this user.')
            data['user'] = user
            data['employee_id'] = employee.id
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        return data