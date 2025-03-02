from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch') # Povolíme POST bez CSRF
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request}) # Pass the request to the serializer
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)  # Log the user in
        return Response(serializer.data, status=status.HTTP_200_OK)