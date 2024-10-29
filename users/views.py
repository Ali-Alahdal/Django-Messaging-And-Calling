from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer ,LoginSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    
    def create(self , request):
    
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username" : user.username,
                "emai" : user.email,
                "message" : "User Registered Successfully."
            } , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Generate or get the token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user_id" : user.id,
                "token": token.key
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)