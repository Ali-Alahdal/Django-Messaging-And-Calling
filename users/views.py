from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response 
from .serializers import RegisterSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def create(self , request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username" : user.username,
                "emai;" : user.email,
                "message" : "User Registered Successfully."
            } , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)